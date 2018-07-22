# 使用Python3基于FFmpeg实现的录制摄像头和屏幕录制
### 1. 运行环境和所需组件
  1. [Python3](https://www.python.org/downloads)
  2. 安装依赖组件，-i是代理地址，使用代理下载速度会加快一点：
```python
pip install -r requirements.txt -i https://pypi.douban.com/simple
```
  3. 录制屏幕需要下载[Screen Capture Recorder](https://sourceforge.net/projects/screencapturer/)
  4. 安装编译工具cx_Freeze（如果需要）。
  ```python
  pip install cx_freeze
  ```
  5. 下载安装打包工具[Inno Setup](http://www.jrsoftware.org/isinfo.php)（如果需要打包）。
### 2.在命令行下运行
```python
python recordwindow.py
#Win10-64系统稳定运行，其他系统暂未测试。
```
### 3.设置
参考设置如下：
* 摄像头名称：USB2.0 HD UVC WebCam
* 声音输入设备：麦克风 (Realtek High Definition Audio)
* 屏幕录制设备：screen-capture-recorder
* 系统声音设备：virtual-audio-capturer

不同机器和设备名称有所不同。
### 4.编译
```
python csetup.py build
#默认编译的可执行文件生成在目录：D:\dev\record\record-win
#参照csetup.py修改编译信息
```
### 5.打包
用Inno setup打开setup.iss文件，修改必要信息，然后编译执行。
