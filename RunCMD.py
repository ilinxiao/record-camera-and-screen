import subprocess   

def run_cmd(cmd, shell = True, universal_newlines = False):
    output_info=[]
    output_err=[]
    with subprocess.Popen(cmd, 
                                                 shell = shell, 
                                                 universal_newlines = universal_newlines, 
                                                 stdout = subprocess.PIPE,
                                                 stdin = subprocess.PIPE,
                                                 stderr = subprocess.PIPE
                                                ) as p:
        while True:
            info=str(p.stdout.read(), encoding ='utf-8')
            # print(dir(p.stderr))
            # print(info)
            err=str(p.stderr.read(), encoding = 'utf-8')
            # print(err)
            if not info and not err:
                if p.poll() is not None:  
                    break
            else:
                output_info.append(info)
                output_err.append(err)
                
    return output_err, output_info
    
        