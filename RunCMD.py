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
    
        