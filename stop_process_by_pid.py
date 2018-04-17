import os,signal

pid = input('输入进程id:')

print(os.kill(int(pid) , signal.CTRL_C_EVENT))