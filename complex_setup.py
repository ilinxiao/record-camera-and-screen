import sys
import traceback
from cx_Freeze import setup, Executable
# import msilib



# Dependencies are automatically detected, but it might need fine tuning.

def get_windows_text(txt):
    # return txt.encode('gbk')
    return txt

#中文需要显式用gbk方式编码
version = '0.2.1'
program_name = u'Gutin谷田会议视频录播管理系统'
program_windows_name = get_windows_text(program_name)
unprogram_windows_name = get_windows_text(u'卸载'+program_name)
program_des = get_windows_text(program_name+u"客户端程序 Ver."+version)
program_icon = "resource/gutin.ico" 
work_dir = 'record-gutin'


#uuid叫通用唯一识别码，后面再卸载快捷方式中要用到
program_code = 'recordwindow'+version

#主程序手动命名

target_name= 'RecordWindow.exe'

build_exe_options = {

    'include_files':['resource','ffmpeg-shared'],        #包含外围的ini、jpg文件，以及data目录下所有文件，以上所有的文件路径都是相对于cxsetup.py的路径。
    # "packages": ["os"],                #包含用到的包
    # "includes": ["PIL","traceback"], 
    # "excludes": ["tkinter"],                #提出wx里tkinter包
    # "path": sys.path,                       #指定上述的寻找路径
    # "icon": program_icon                       #指定ico文件
};



#快捷方式表，这里定义了三个快捷方式

shortcut_table = [

     

     #1、桌面快捷方式

    (program_windows_name,           # Shortcut

     "DesktopFolder",             # Directory_ ，必须在Directory表中

     program_windows_name,                # Name

     "TARGETDIR",                 # Component_，必须在Component表中

     "[TARGETDIR]"+target_name,   # Target

     None,                        # Arguments

     program_des,                # Description

     None,                        # Hotkey

     program_icon,                        # Icon

     None,                        # IconIndex

     None,                        # ShowCmd

     'TARGETDIR'                  # WkDir

     ),

    

    #2、开始菜单快捷方式

    (program_windows_name,           # Shortcut

     "MenuDir",                   # Directory_

     program_windows_name,                # Name

     "TARGETDIR",                 # Component_

     "[TARGETDIR]"+target_name,   # Target

     None,                        # Arguments

     program_des,                # Description

     None,                        # Hotkey

     program_icon,                        # Icon

     None,                        # IconIndex

     None,                        # ShowCmd

     'TARGETDIR'                  # WkDir

     ),

    

    #3、程序卸载快捷方式

    (unprogram_windows_name,              # Shortcut

     "MenuDir",                  # Directory_

     unprogram_windows_name,             # Name

     "TARGETDIR",                # Component_

     "[System64Folder]msiexec.exe",  # Target

     r"/x"+program_code,         # Arguments

     program_des,               # Description

     None,                       # Hotkey

     None,                       # Icon

     None,                       # IconIndex

     None,                       # ShowCmd

     'TARGETDIR'                 # WkDir

     )      

    ]





#手动建设的目录，在这里定义。

'''

自定义目录说明：

==============

1、3个字段分别为 Directory,Directory_Parent,DefaultDir

2、字段1指目录名，可以随意命名，并在后面直接使用

3、字段2是指字段1的上级目录，上级目录本身也是需要预先定义，除了某些系统自动定义的目录，譬如桌面快捷方式中使用DesktopFolder

参考网址 https://msdn.microsoft.com/en-us/library/aa372452(v=vs.85).aspx

'''

directories = [

     ( "ProgramMenuFolder","TARGETDIR","." ),

     ( "MenuDir", "ProgramMenuFolder", work_dir)

     ]



# Now create the table dictionary

# 也可把directories放到data里。

'''

快捷方式说明：

============

1、windows的msi安装包文件，本身都带一个install database，包含很多表（用一个Orca软件可以看到）。

2、下面的 Directory、Shortcut都是msi数据库中的表，所以冒号前面的名字是固定的(貌似大小写是区分的)。

3、data节点其实是扩展很多自定义的东西，譬如前面的directories的配置，其实cxfreeze中代码的内容之一，就是把相关配置数据写入到msi数据库的对应表中

参考网址：https://msdn.microsoft.com/en-us/library/aa367441(v=vs.85).aspx

'''

msi_data = {#"Directory":directories ,

            "Shortcut": shortcut_table 

          }



# Change some default MSI options and specify the use of the above defined tables

#注意product_code是我扩展的，现有的官网cx_freeze不支持该参数，为此简单修改了cx_freeze包的代码，后面贴上修改的代码。

bdist_msi_options = {
                        # 'data': msi_data,
                        'add_to_path': False,
                        'directories': directories,
                        'initial_target_dir': r'[ProgramFilesFolder]\%s' % (work_dir)}

                      



# GUI applications require a different base on Windows (the default is for a

# console application).

base = None;

if sys.platform == "win32":

     base = "Win32GUI"



#简易方式定义快捷方式，放到Executeable()里。

#shortcutName = "AppName",

#shortcutDir = "ProgramMenuFolder" 

setup(  
        name = program_windows_name.encode('gbk'),
        author='林潇',
        version = version,
        description = program_des,
        options = {"build_exe": build_exe_options,"bdist_msi": bdist_msi_options},
        executables = [Executable(
                                    "RecordWindow.py",
                                    targetName= target_name,
                                    base=base,
                                    icon = program_icon)
                                  ])