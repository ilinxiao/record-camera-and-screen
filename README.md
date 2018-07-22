# 使用Python3基于FFmpeg实现的录制摄像头和屏幕录制及方便的在两者之间切换
### 两种运行方式
一、 在命令行下执行源代码
二、 打包成完整的安装程序
### 1. 在命令行下执行环境和所需组件
  1. [Python3](https://www.python.org/downloads)
  2. 安装依赖组件，-i是代理地址，使用代理下载速度会加快一点：
```python
pip install -r requirements.txt -i https://pypi.douban.com/simple
```
  3. 录制屏幕需要下载[Screen Capture Recorder](https://sourceforge.net/projects/screencapturer/)
### 2.在命令行下运行
```python
python recordwindow.py
#Win10-64系统稳定运行，其他系统暂未测试。
```
