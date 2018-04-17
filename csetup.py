import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = { 'include_files':['resource']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
directories = [
     ( "resource","."),
     ]    
executables = [
    Executable('RecordWindow.py', base=base)
]
setup(  name = "recordwindow",
        version = "0.1",
        description = "record camera or screen",
        options = {"build_exe": build_exe_options},
        executables=executables,
        directories = directories
        )