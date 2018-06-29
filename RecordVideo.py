import datetime,time,sys,os,signal,re,winreg
from datetime import datetime
import subprocess,threading
from subprocess import CalledProcessError
# from multiprocessing import Process
from threading import Thread
import ctypes,inspect
import RecordType
from RecordType import *
import RecordConfig
from RecordConfig import *
import logging
import RunCMD
from RunCMD import get_ffmpeg_path
from winreg import HKEY_CURRENT_USER, OpenKey, QueryInfoKey, EnumValue, SetValueEx, CloseKey, REG_SZ, KEY_READ, KEY_SET_VALUE

class RecordVideo():


    '''
        ffmpeg -f dshow -i video="@device_pnp_\\\\?\\usb#vid_04f2&pid_b354&mi_00#7&30d7ad30&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global":audio="@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{571529B3-7DB3-42A3-ADEF-BBD82925C15D}" -acodec libmp3lame -vcodec libx265 -preset:v ultrafast -tune:v zerolatency -s 1920x1080 -r 7 -y record_camera_20180408_182541.mkv
        
    '''    
    
    def __init__(self, record_video=True, record_voice=True):
        # print('视频录制初始化中...')
        # self.record_video=record_video
        # self.record_voice=record_voice
        #录制状态
        self.recording = False
        self.exception_exit = False
        self.record_type=RecordType.Camera
        #文件名称
        self.file_name='record'
        #文件后缀
        self.file_suffix='.mkv'
        self.process = None
        self.record_thread_name='record'
        self.record_thread=None
        
        self.file_dir = ''
        self.load()
        
    def load(self):
        #日志
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level = logging.INFO)
        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)    
        
        self.logger.addHandler(handler)
        
        self.load_config()
        
        
    def load_config(self):
  
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
        #线程数
        self.threads = rc.config.getint('record','threads')
        
        self.logger.info('camera device name: %s' % self.camera_name)
        self.logger.info('voice device name: %s' % self.voice_device_name)
        self.logger.info('screen device name: %s' % self.screen_name)
        self.logger.info('system voice device name: %s' % self.system_voice_device_name)
        self.logger.info('vcodec: %s' % self.video_codec)
        self.logger.info('resolution: %s' % self.resolution)
        self.logger.info('frame rate: %s' % self.brate)
        self.logger.info('save dir: %s' % self.file_dir)
        
        
    def start_ffmpeg(self,cmd, shell = True):
    
        try:
            print('录制中...')
            self.logger.info('录制中...')
            # print('cmd:\n%s' % cmd)
            start_time = datetime.now()
            self.process=subprocess.Popen(cmd, shell=shell, universal_newlines = True, stdin = subprocess.PIPE, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
            line = ''
            while self.recording:
                
                # print(cmd)
                # print(self.recording)
                # tmp_out = self.process.stdout.readline()
                line += str(self.process.stdout.readline())
                # print('test tmp out:%s' % tmp_out)
                #文字输出编码错误记录
                #异常：UnicodeDecodeError: 'gbk' codec can't decode byte 0xb4 in position 2881: illegal multibyte sequence
                #原因：cmd输出包含中文字符
                #解决方案：universal_newlines = False
                #缺陷：需要以字节形式的q来控制退出:write(b'q')
                #最终原因及解决方案：引起gbk编码错误的原因是文件名的中文与数字的连接符号由下划线'_'改成了横杠'-'。
                #为什么这个修改会引起运行时ffmpeg报编码错误，推测终究还是ffmpeg对中文编码的支持问题。
                #最终方案即文件名中的中文后的连接符号改回下划线。
                
                now = datetime.now()
                if (now - start_time).total_seconds() >2:
                    # self.logger.info('recording...')
                    ffmpeg_running = False
                    if self.process:
                        ffmpeg_running = self.process.poll() is None
                        log_text = 'ffmpeg 运行状态:%s' % ('运行中' if ffmpeg_running else '终止')
                        
                        print(log_text)
                        self.logger.info(log_text) 
                        
                    else:
                        txt= 'ffmpeg子进程已终止.'
                        print(txt)
                        self.logger.warning(txt)
                     
                    if not ffmpeg_running:
                        
                        print(self.process.communicate())
                        raise CalledProcessError(self.process.returncode, cmd)
                    
                    # self.logger.info(line)
                    print(line)
                    line = ''
                    start_time = now
                    
                # print(line)
                
                if not self.recording:
                    self.process.stdin.write('q')
                    print(self.process.communicate())
                    break
        
        except CalledProcessError as e:
            log_txt = 'ffmpeg异常终止:\nreturn code: %d\ncmd:\n%s' % (e.returncode, e.cmd)
            print(log_txt)
            self.logger.warning(log_txt)      
            self.recording = False
            self.exception_exit = True
            print('process is None?:%s' % (self.process is None))
            # self.stop_record()
        except Exception as x:
            print('未捕获的异常：')
            print(x)
        # self.logger.info(self.process.communicate())
        # print('over')
        
    def record(self, cmd='ffmpeg -h', target = None):
       
       if target:
            cmd = os.path.join(get_ffmpeg_path(), cmd)
            print('cmd: \n%s' % cmd)
            self.logger.info('record cmd:\n %s' % cmd)
            self.record_thread = Thread(name=self.record_thread_name, target= target, args = (cmd,), daemon=True)
            self.record_thread.start()
            self.recording=True
            self.exception_exit = False
            
            print('record thread,ident:%d' % self.record_thread.ident)
            # th.join()
                
    def stop_record(self):
        
        # print('threading active thread count:%d' % threading.active_count())
        try:
            
            self.recording = False
            self.logger.info('录制将停止...')
            if self.process:
                self.logger.info('ffmpeg进程状态: %s' % (self.process.poll() is not None))
                if self.process.returncode:
                    print('subprocess return code:%d' % self.process.returncode)
            print('record thread status: %s' % self.record_thread.is_alive())
            
            if self.record_thread.is_alive():
                
                self.record_thread.join(1)
            print('record thread status: %s' % self.record_thread.is_alive())
        except (Exception,KeyboardInterrupt) as e:
            print('kill exception:\n %s' % e)
            self.logger.warning('kill exception:\n %s' % e)
        
    def record_camera(self):

        if self.camera_name and self.voice_device_name:
            
            self.record_type=RecordType.Camera
            record_cmd='ffmpeg -f dshow -i video=\"%s\":audio=\"%s\" -acodec libmp3lame -vcodec %s -preset:v ultrafast -tune:v zerolatency -s %s -r %d -threads %d -y %s' %(
            self.deal_with_device_name(self.camera_name),
            self.deal_with_device_name(self.voice_device_name),
            self.video_codec,
            self.resolution,
            self.brate,
            self.threads,
            self.get_file_name()
            )
            # print(record_cmd)
            self.record(record_cmd, self.start_ffmpeg)
        
    def record_screen(self):
        if self.screen_name and self.system_voice_device_name:
            self.record_type=RecordType.Screen
            record_cmd='ffmpeg -f dshow -i video="{}":audio="{}" -acodec libmp3lame -vcodec {} -preset:v ultrafast -tune:v zerolatency -s {} -r {} -threads {} -y {}'.format(
            self.deal_with_device_name(self.screen_name),
            self.deal_with_device_name(self.system_voice_device_name),
            self.video_codec,
            '1024x768', #屏幕录制分辨率固定
            self.brate,
            self.threads,
            self.get_file_name()
            )
            self.record(record_cmd, self.start_ffmpeg)    
    
    def check_device(self):
        #简单验证摄像头设置是否为空
        ready = True
        l_msg = ''
        if not self.camera_name:
            ready = False
            l_msg += '摄像头设备为空\n'
        
        if not self.voice_device_name:
            ready = False
            l_msg += '麦克风设备为空\n'
           
        if not self.screen_name:
            ready = False
            l_msg += '屏幕录制驱动为空\n'
        
        if not self.system_voice_device_name:
            ready = False
            l_msg += '系统声音录制驱动为空\n'
        
        if ready:
            l_msg = '设备检测正常'
        print(l_msg)
        self.logger.info(l_msg)
        return ready
                    
             
    def check_run_state(self):
        #验证运行有效性逻辑：
        #一、判断是否正常安装
        #判断条件：软件安装时在注册表“HKEY_CURRENT_USER\\SOFTWARE\\Gutin\\Record“记录下安装目录
        #二、非正常安装有效时间为三个月,且只能发生一次
        
        #验证当前运行目录是否存在注册表中
        qualified = False
        run_dir = os.path.abspath('.')
        # print('run_dir:%s' % run_dir)
        reg_path = 'SOFTWARE\\Gutin\\Record'
        feature_name ='InstallDir'
        key = OpenKey(HKEY_CURRENT_USER, reg_path, access = KEY_READ)
        items = QueryInfoKey(key)
        for i in range(items[1]):
            item = EnumValue(key, i)
            name = item[0]
            value = item[1]
            type = item[2]
            if name and name.find(feature_name)>=0:
                if os.path.samefile(value, run_dir):
                    qualified = True
                    break;
        
        if not qualified:
            #查找非正常安装目录记录
            #记录以运行目录的hash值作为键名，值为首次运行的时间
            time_format= '%Y-%m-%d %H:%M:%S'
            run_time = None
            unqualified_key_name  = 'Unqualified'
            has_unqualified = False
            for i in range(items[1]):
                item = EnumValue(key, i)
                name = item[0]
                value = item[1]
                type = item[2]
                if name == unqualified_key_name:
                    has_unqualified = True
                    run_time = value
          
            if not has_unqualified:
                #如果不存在，创建       
                run_time = datetime.now().strftime(time_format)
                key = OpenKey(HKEY_CURRENT_USER, reg_path, access = KEY_SET_VALUE)
                SetValueEx(key, unqualified_key_name, 0, REG_SZ, run_time)            
                      
            #判断时限
            # now = datetime.strptime('2018-06-22 12:11:51', time_format)
            now = datetime.now()
            run_time_obj = datetime.strptime(run_time, time_format)
            print('first run_time:%s' % run_time)
            print('now:%s' % now.strftime(time_format))
            
            qual_days = 91 - (now - run_time_obj).days
            # print('qualified days:%d' % (qual_days))
            # qual_hours = (now - run_time_obj).total_seconds() // 3600
            if qual_days > 0:
            # if 5 - qual_hours > 0:
                qualified = True
         
        CloseKey(key)
        return qualified

    
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
        date_dir = datetime.now().strftime('%Y-%m-%d')
        time_str = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        video_type_name = ''
        if self.record_type == RecordType.Camera:
            # video_type_name = 'camera'
            video_type_name = '摄像头'
        if self.record_type == RecordType.Screen:
            video_type_name = '屏幕'
            # video_type_name = 'screen'
        
        today_file_dir = os.path.join(self.file_dir, date_dir)
        if not os.path.exists(today_file_dir):
            os.mkdir(today_file_dir)
        file_name = os.path.join(today_file_dir, '{}_{}{}'.format(video_type_name, time_str, self.file_suffix))
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
        
        