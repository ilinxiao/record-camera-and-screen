import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = { 'include_files':['resource','ffmpeg-shared']}
install_exe_options = { 'install_dir' : 'd:\\record-camera-and-screen', 'build_dir':'build', 'install_exe':'d:\\record-camera-and-screen'}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
executables = [
    Executable('RecordWindow.py', base=base, icon = 'resource/gutin.ico', targetName = 'RecordWindow.exe')
]
setup(  name = "Gutin谷田会议视频录播管理系统",
        version = "0.2",
        description = "record camera or screen",
        options = {"build_exe": build_exe_options},
        executables=executables
        )