import subprocess,os,sys

def run_cmd(cmd, shell = True, universal_newlines = False):
    output_info=[]
    output_err=[]
    cmd = os.path.join(get_ffmpeg_path(), cmd)
    print('执行cmd：\n%s' % cmd)
    with subprocess.Popen(cmd, 
                                                 shell = shell, 
                                                 universal_newlines = universal_newlines, 
                                                 stdout = subprocess.PIPE,
                                                 stdin = subprocess.PIPE,
                                                 stderr = subprocess.PIPE
                                                ) as p:
        while True:
            info=p.stdout.read()
            # print(dir(p.stderr))
            print(info)
            err=p.stderr.read()
            print(err)
            # if not info and not err:
            if info == b'' and err == b'':
                if p.poll() is not None:  
                    break
            else:
                output_info.append(info)
                output_err.append(err)
                
    return output_err, output_info
    
        
def get_ffmpeg_path():
    
    datadir = ''
    subdir = os.path.join('ffmpeg-shared','bin')
    
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    datadir = os.path.join(datadir, subdir)
    datadir = os.path.abspath(datadir)
    print(datadir)
    #如果存在ffmpeg.exe
    if os.path.isfile(os.path.join(datadir, 'ffmpeg.exe')):
        return datadir
    #兼容环境变量设置
    return ''
    
        