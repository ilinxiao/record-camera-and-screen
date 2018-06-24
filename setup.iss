; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

#define MyAppName "Gutin谷田会议视频录播管理系统"
#define MyAppVersion "0.3"
#define MyAppPublisher "珠海市谷田音频科技有限公司"
#define MyAppExeName "RecordWindow.exe"

[Setup]
; 注: AppId的值为单独标识该应用程序。
; 不要为其他安装程序使用相同的AppId值。
; (生成新的GUID，点击 工具|在IDE中生成GUID。)
AppId={{B91CC43B-FF1E-4169-B77C-1B259E89F014}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
;AppPublisherURL={#MyAppURL}
;AppSupportURL={#MyAppURL}
;AppUpdatesURL={#MyAppURL}
DefaultDirName=d:\gutin-record
DefaultGroupName=Gutin谷田会议视频录播管理系统
AllowNoIcons=yes
OutputDir=D:\dev\record\out-test
OutputBaseFilename=Gutin谷田会议视频录播管理系统-{#MyAppVersion}
SetupIconFile=C:\Users\lv\ctest\record-camera-and-screen\resource\gutin.ico
Compression=lzma
SolidCompression=yes

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "startupicon"; Description: "开机启动"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked 

[Files]
Source: "D:\dev\record\record-win\RecordWindow.exe"; DestDir: "{app}"; Flags: ignoreversionSource: "D:\dev\record\record-win\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
;Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon
Name: "{userstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startupicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent


[Registry]
Root: HKCU; Subkey: "SOFTWARE\Gutin\Record"; ValueType:string; ValueName: "InstallDir{#GetDateTimeString('dd/mm/yyyy hh:nn:ss', '-', ':')}"; ValueData: "{app}"; Flags: uninsdeletevalue createvalueifdoesntexist;
;遇到的问题HKLM节点无法写入
;Root: HKCU; Subkey: "Software\My Company Test"; Flags: uninsdeletekeyifempty



