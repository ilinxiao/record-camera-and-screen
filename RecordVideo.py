import datetime,time,sys,os,signal,re
from datetime import datetime
import subprocess,threading
# from multiprocessing import Process
from threading import Thread
import ctypes,inspect
import RecordType
from RecordType import *
import RecordConfig
from RecordConfig import *
import logging
import RunCMD
from RunCMD import run_cmd

class RecordVideo():


    '''
        ffmpeg -f dshow -i video="@device_pnp_\\\\?\\usb#vid_04f2&pid_b354&mi_00#7&30d7ad30&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global":audio="@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{571529B3-7DB3-42A3-ADEF-BBD82925C15D}" -acodec libmp3lame -vcodec libx265 -preset:v ultrafast -tune:v zerolatency -s 1920x1080 -r 7 -y record_camera_20180408_182541.mkv
        
    '''    
    
    def __init__(self, record_video=True, record_voice=True):
        # print('视频录制初始化中...')
        # self.record_video=record_video
        # self.record_voice=record_voice
        #录制状态
        self.recording=False
        self.record_type=RecordType.Camera
        #文件名称
        self.file_name='record'
        #文件后缀
        self.file_suffix='.mkv'
        self.process = None
        self.record_thread_name='record'
        self.record_thread=None
        
        self.file_dir = ''
        self.load_config()
        
    
    def load_config(self):
        
        #日志
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level = logging.INFO)
        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
        
        rc = RecordConfig()
        self.config = rc.config
        
        #摄像头名称
        self.camera_name=rc.config.get('devices','camera_device_name')
        #麦克风名称
        self.voice_device_name=rc.config.get('devices','voice_device_name')
        #录制屏幕名称
        self.screen_name=rc.config.get('devices','screen_device_name')
        #系统声音设备名称
        self.system_voice_device_name=rc.config.get('devices','system_voice_device_name')
        #视频编码
        self.video_codec=rc.config.get('record','vcodec')
        #分辨率
        self.resolution=rc.config.get('record','resolution')
        #帧率
        self.brate=rc.config.getfloat('record','frame_rate')
        #文件目录
        self.file_dir= os.path.abspath(rc.config.get('record','file_dir'))
        
        self.logger.info('camera device name: %s' % self.camera_name)
        self.logger.info('voice device name: %s' % self.voice_device_name)
        self.logger.info('screen device name: %s' % self.screen_name)
        self.logger.info('system voice device name: %s' % self.system_voice_device_name)
        self.logger.info('vcodec: %s' % self.video_codec)
        self.logger.info('resolution: %s' % self.resolution)
        self.logger.info('frame rate: %s' % self.brate)
        self.logger.info('save dir: %s' % self.file_dir)
        
    def start_ffmpeg(self,cmd, shell = True):
        print('录制中...')
        self.logger.info('录制中...')
        # print('cmd:\n%s' % cmd)
        start_time = datetime.now()
        self.process=subprocess.Popen(cmd, shell=shell, universal_newlines = True, stdin = subprocess.PIPE, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
        # print(self.process.stdin)
        line = ''
        while self.recording:
        
            line += self.process.stdout.readline()
            now = datetime.now()
            if (now - start_time).total_seconds() >2:
                # self.logger.info('recording...')
                if self.process:
                    log_text = 'ffmpeg 运行状态:%s' % ('终止' if (self.process.poll() is not None) else '运行中')
                    print(log_text)
                    self.logger.info(log_text) 
                    
                else:
                    print('ffmpeg子进程已终止.')
                # self.logger.info(line)
                print(line)
                line = ''
                start_time = now
                
            # print(line)
            
            if not self.recording:
                self.process.stdin.write('q')
                print(self.process.communicate())
                break
                
        # self.logger.info(self.process.communicate())
        # print('done.')
        
    def record(self,cmd='ffmpeg -h', target = None):
       
       if target:
            print('cmd: \n%s' % cmd)
            self.logger.info('record cmd:\n %s' % cmd)
            th=Thread(name=self.record_thread_name, target= target, args = (cmd,), daemon=True)
            th.start()
            self.record_thread=th
            print('record thread,ident:%d' % self.record_thread.ident)
            self.recording=True
            
    def stop_record(self):
        
        # print('threading active thread count:%d' % threading.active_count())
        try:
            
            self.recording = False
            self.logger.info('ffmpeg pid: %d' % self.process.pid)
            self.logger.info('录制将停止...')
            self.logger.info('ffmpeg进程状态: %s' % (self.process.poll() is not None))
            self.recording=False
            if self.record_thread.is_alive():
                self.record_thread.join(1)
            print('record thread status: %s' % self.record_thread.is_alive())
        except (Exception,KeyboardInterrupt) as e:
            print('kill exception:\n %s' % e)
            self.logger.warning('kill exception:\n %s' % e)
        
    def record_camera(self):

        if self.camera_name and self.voice_device_name:
            
            self.record_type=RecordType.Camera
            record_cmd='ffmpeg -f dshow -i video=\"%s\":audio=\"%s\" -acodec libmp3lame -vcodec %s -preset:v ultrafast -tune:v zerolatency -s %s -r %d -y %s' %(
            self.deal_with_device_name(self.camera_name),
            self.deal_with_device_name(self.voice_device_name),
            self.video_codec,
            self.resolution,
            self.brate,
            self.get_file_name()
            )
            # print(record_cmd)
            self.record(record_cmd, self.start_ffmpeg)
        
    def record_screen(self):
        if self.screen_name and self.system_voice_device_name:
            self.record_type=RecordType.Screen
            record_cmd='ffmpeg -f dshow -i video="{}":audio="{}" -acodec libmp3lame -vcodec {} -preset:v ultrafast -tune:v zerolatency -s {} -r {} -y {}'.format(
            self.deal_with_device_name(self.screen_name),
            self.deal_with_device_name(self.system_voice_device_name),
            self.video_codec,
            self.resolution,
            self.brate,
            self.get_file_name()
            )
            self.record(record_cmd, self.start_ffmpeg)    

            
    def debug_camera(self):
        try:
            play_cmd = ['ffplay','-f','dshow','-i','video={}'.format(self.camera_name),'-window_title','按q退出','-noborder']
            self.record(play_cmd, self.play)
        except Exception as e:
            print(e)
        
    def play(self, cmd):
        try:
            t_process=subprocess.Popen(cmd, shell= False, universal_newlines = True, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
            while True:
                 line = t_process.stdout.readline()
                 print(line)
                 if line == '':
                    if t_process.poll() is not None:
                        break               
            t_process.communicate()
        except (Exception, KeyboardInterrupt) as e:
            print(e)
            
    def deal_with_device_name(self,device_name):    
        # print(device_name)
        # new_name=device_name.replace('\\','\\\\')
        # print(new_name)
        # return new_name
        return device_name
        
    def get_file_name(self):
        time_str=datetime.now().strftime('%Y%m%d_%H%M%S')
        video_type = ''
        if self.record_type == RecordType.Camera:
            video_type = '摄像头'
        if self.record_type == RecordType.Screen:
            video_type = '屏幕'
        
        file_name = os.path.join(self.file_dir, '{}_{}{}'.format(video_type, time_str, self.file_suffix))
        print('recording file name: %s' % file_name)
        return file_name
        
    def _async_raise(self, tid, exctype):  
        """raises the exception, performs cleanup if needed"""  
        tid = ctypes.c_long(tid)  
        if not inspect.isclass(exctype):  
            exctype = type(exctype)  
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))  
        print('async_raise res value:%d' % res)
        if res == 0:  
            raise ValueError("invalid thread id")  
        elif res != 1:  
            # """if it returns a number greater than one, you're in trouble,  
            # and you should call it again with exc=NULL to revert the effect"""  
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)  
            raise SystemError("PyThreadState_SetAsyncExc failed")  
    
    def kill_process(self, process_name='ffmpeg'):
            cmd='tasklist | findstr {}'.format(process_name)
            output_strs, output_errs=self.run_cmd(cmd)
            pid=[]
            if output_strs:
                print('find "%s" result: \n%s' % (process_name, ''.join(output_strs)))
                for output_str in output_strs:
                    find_re=re.search(r'({}.+?)\s*([0-9]+)'.format(process_name),output_str)
                    if find_re:
                        full_process_name=find_re.group(1).strip()
                        pid=find_re.group(2).strip()
                        print('计划结束任务：{}@pid： {}'.format( full_process_name, pid ))
                        task_kill_cmd = 'taskkill /T /F /pid {}'.format(pid)
                        # status, output = subprocess.getstatusoutput(task_kill_cmd)
                        
                        # if status == 1:
                            # print('任务成功被结束:')
                        # else:
                            # print('任务结束失败:')
                        # print(output)   
                
            else:
                print('not found task about "%s" in tasklist' % process_name )
    
 
        # def stop_thread(self,thread):  
        # self._async_raise(thread.ident, SystemExit)  
        
        