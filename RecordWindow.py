import sys, datetime
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QMessageBox
import RecordVideo,RecordType
from RecordVideo import *
from RecordType import *
import SettingWindow
from SettingWindow import *
import Shortcut
from Shortcut import *
import RecordTrayIcon
from RecordTrayIcon import *
import RecordConfig
from RecordConfig import *
import RecordHelp
from RecordHelp import *

class RecordWindow(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super(RecordWindow,self).__init__(parent) 
        self.setupUi()
        self.load_modules()
        #更新设置
        self.need_update_config = False
        self.need_hide = True
        #初始化状态
        print('初始化状态...')
        self.update_state()
        
    def load_modules(self):
        #录制
        self.rv=RecordVideo()      
        #鼠标拖动
        self.m_drag = False
        #托盘图标
        self.rti = RecordTrayIcon(self)
        self.rti.update_state(self.recording, self.record_type)
        
        self.rc = RecordConfig()
        
        self.file_dir = self.rc.config.get('record','file_dir')
        # self.debugCameraAction.triggered.connect(self.rv.debug_camera)
        
    def closeEvent(self, event):
        # print('close window.')
        # self.close_signal.emit()
        # self.close()
        # if self.recording:
        
            # question = QMessageBox(self)
            # question.setText('系统正在录制中，确定要退出吗？')
            # question.setWindowTitle('提示')
            # question.setIcon(QMessageBox.Question)
            # question.addButton(QMessageBox.Yes)
            # question.addButton(QMessageBox.No)
            # question.setDefaultButton(QMessageBox.No)
            # ret = question.exec()
            # if ret == QMessageBox.Yes:
                # self.stop_record()
                # QCoreApplication.instance().quit()
                
        # else:
            
            # question = QMessageBox()
            # question.setText('确定要退出吗？')
            # question.setWindowTitle('提示')
            # question.setIcon(QMessageBox.Question)
            # question.addButton(QMessageBox.Yes)
            # question.addButton(QMessageBox.No)
            # question.setDefaultButton(QMessageBox.No)
            # ret = question.exec()
            # if ret == QMessageBox.Yes:
        
        print('软件将退出.')
        QCoreApplication.instance().quit()
                
        # event.ignore()
                
                
        
    def setupUi(self):
        self.setObjectName("RecordWindow")
        self.resize(94, 81)
        self.move(1100,600)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(0, 30, 91, 51))
        self.pushButton.setObjectName("pushButton")
        # self.register_slot(self.pushButton.clicked, self.record)
        # self.pushButton.mousePressEvent.connect(self.mousePressEvent)
        # print(dir(self.pushButton))
        
        #添加右键菜单
        self.createContextMenu()
        
        #添加计时器
        self.lcd = QLCDNumber(self)      
        self.lcd.setDigitCount(10)      
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setGeometry(QtCore.QRect(0, 0, 91, 31))
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.init_lcd()
        
        #新建一个QTimer对象        
        self.timer = QTimer()      
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self.onTimerOut)
         
        self.retranslateUi()
        
        #调整窗体属性       
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        # self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.installEventFilter(self)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("RecordWindow", "RecordWindow"))
        self.pushButton.setText(_translate("RecordWindow", "开始"))

        
    def init_lcd(self):       
        self.lcd.display('0:00:00')   
        
    def start_timer(self):      
        self.start_time = datetime.now()
        self.init_lcd()
        self.timer.start()
    
    def stop_timer(self):
        self.timer.stop()
        self.init_lcd()
             
     # 刷新录制时间
    def onTimerOut(self):       
        print('on timer out monitor record status :%s' % self.recording)
        if self.recording:
            self.lcd.display(self.get_display_time(self.start_time))
        else:
            # self.stop_timer()
            self.stop_record(force  = self.exception_exit)
            
            if self.exception_exit:
                time.sleep(2)
                self.record(self.record_type)
        
    def get_display_time(self,old_time):
        delta_time = datetime.now() - old_time
        delta_time_str = str(delta_time)
        pos = delta_time_str.find('.')
        time_text = delta_time_str[0:pos]
        return time_text  
     
    #打开文件目录
    def open_file_dir(self):
        dirpath = self.file_dir
        if os.path.isdir(dirpath):
            os.startfile(dirpath)
        else:
            print('错误的文件目录：%s' % dirpath)
        
     #显示菜单
    def showContextMenu(self):
        self.contextMenu.exec_(QtGui.QCursor.pos())
            
    #添加右键菜单
    def createContextMenu(self):
        #更改右键菜单为自定义
        print('初始化右键菜单...')
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        
        self.contextMenu = QtWidgets.QMenu(self)
        #停止/开始录制
        self.recordSwitchAction = self.contextMenu.addAction('开始/停止录制')
        #开始录制摄像头
        self.recordCameraAction = self.contextMenu.addAction('开始录制摄像头')
        #录制屏幕
        self.recordScreenAction = self.contextMenu.addAction('开始录制屏幕')        
        #分隔栏
        self.separatorAction = self.contextMenu.addAction('分隔栏')
        self.separatorAction.setSeparator(True)       
        self.openFileDirAction = self.contextMenu.addAction('打开文件目录')
        self.openFileDirAction.triggered.connect(self.open_file_dir)
        #调试摄像头
        # self.debugCameraAction = self.contextMenu.addAction('调试摄像头')
        # self.debugCameraAction.setVisible(False)
        #设置
        self.settingAction=self.contextMenu.addAction('设置')    
        self.sw = SettingWindow()
        self.settingAction.triggered.connect(self.show_setting)  
        #帮助
        self.aboutAction=self.contextMenu.addAction('帮助')    
        self.rh = RecordHelp()
        self.aboutAction.triggered.connect(self.rh.showWindow)
        #退出
        self.exitAction = self.contextMenu.addAction('退出')
        self.exitAction.triggered.connect(self.close)
    
    
    '''
        功能事件
     
     
    '''
     
    @property
    def recording(self):
        return self.rv.recording
    @property
    def exception_exit(self):
        return self.rv.exception_exit
    @property
    def record_type(self):
        return self.rv.record_type
     
    def register_slot(self, event_obj, new_action, disconnect = True):
        if disconnect:
            try:
                event_obj.disconnect()
            except Exception as e:
                pass
        event_obj.connect(new_action)
        
    def update_state(self):
        
        if self.recording:
            print('录制状态：录制中.')
            
            if self.record_type == RecordType.Camera:
                print('正在录制摄像头.')
            else:
                print('正在录制屏幕.')
        print('recording:%s' % self.recording)
        print('record_type:%s' % self.record_type)
        
        if self.recording:
            self.recordSwitchAction.setText('停止录制')
            self.register_slot(self.pushButton.clicked, self.stop_record)
            self.register_slot(self.recordSwitchAction.triggered, self.stop_record)
            
            #正在录制摄像头
            if self.record_type == RecordType.Camera:
                self.pushButton.setText('正在录制摄像头\n点击停止')
                self.recordCameraAction.setText('停止录制摄像头')
                self.register_slot(self.recordCameraAction.triggered, self.stop_record)
                
                self.recordScreenAction.setText('开始录制屏幕')
                self.register_slot(self.recordScreenAction.triggered, lambda: self.record(RecordType.Screen))
            #正在录制屏幕
            if  self.record_type == RecordType.Screen:
                
                self.pushButton.setText('正在录制屏幕\n点击停止')
                self.recordScreenAction.setText('停止录制屏幕')
                self.register_slot(self.recordScreenAction.triggered, self.stop_record)
                
                self.recordCameraAction.setText('开始录制摄像头')
                self.register_slot(self.recordCameraAction.triggered, lambda: self.record(RecordType.Camera))
            
        else: 
            self.pushButton.setText('开始')
            self.recordSwitchAction.setText('开始录制')
            self.register_slot(self.pushButton.clicked, lambda: self.record(self.record_type))       
            self.register_slot(self.recordSwitchAction.triggered, lambda: self.record(self.record_type))
        
            self.recordScreenAction.setText('开始录制屏幕')
            self.register_slot(self.recordScreenAction.triggered, lambda: self.record(RecordType.Screen))
            
            self.recordCameraAction.setText('开始录制摄像头')
            self.register_slot(self.recordCameraAction.triggered, lambda: self.record(RecordType.Camera))
            
        self.rti.update_state(self.recording, self.record_type)
    
    def stop_record(self, force = False):
    
        if self.recording or force:
            self.stop_timer()    
            
            if self.record_type == RecordType.Camera:
                print('停止录制摄像头.')
            
            if self.record_type == RecordType.Screen:
                print('停止录制屏幕.')
            
            try:
                self.rv.stop_record()
            except KeyboardInterrupt as e:
                print(e)
            finally:  
                self.update_state()
        # else:
            # exit_tip = '系统即将退出'
            # print(exit_tip)
            # 退出系统
            # self.close()
        
    def record(self, rtype):
        
        if self.recording:            
            if rtype == self.record_type:
                return True
                
            print('检测到正在录制，录制类型将切换...')   
            self.stop_record()
            
        if self.rv.check_device():
            #开始录制
            if rtype == RecordType.Camera:
                print('开始录制摄像头...')
                self.rv.record_camera()
            elif rtype == RecordType.Screen:
                print('开始录制屏幕...')
                self.rv.record_screen()
            
            self.start_timer()
            self.update_state()
        else:
            self.need_hide = False
            question = QMessageBox.information(self, '提示', '检测到录制设备缺失，无法进行录制，请先完善设备设置。', QMessageBox.Yes)
            # self.need_hide = True
            # question = QMessageBox()
            # question.setText('检测到录制设备缺失，无法进行录制，请先完善设备设置。')
            # question.setWindowTitle('提示')
            # question.setIcon(QMessageBox.Question)
            # question.addButton(QMessageBox.Yes)
            # question.addButton(QMessageBox.No)
            # question.setDefaultButton(QMessageBox.No)
            # ret = question.exec()
            # if ret == QMessageBox.Yes:
                # print('软件将退出.')
                
    def show_setting(self):
        self.need_hide = False
        self.sw.showSettingWindow()

    ''''
        鼠标拖动窗体

    '''
        
    def mousePressEvent(self, e):
        if not isinstance(self,RecordWindow):
            e.ignore()
        else:    
            if e.button() == Qt.LeftButton:
                self.m_drag = True
                self.m_DragPosition = e.globalPos() - self.pos()
                e.accept()
                self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))

    def mouseReleaseEvent(self, e):
        if not isinstance(self,RecordWindow):
            e.ignore()
        else:    
            if e.button() == Qt.LeftButton:
                self.m_drag = False
                self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, e):
        if not isinstance(self,RecordWindow):
            e.ignore()
        else:    
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept() 
                
        # print('(x:%d/y:%d)' % (self.x(),self.y()))

    '''
        快捷键监听
        
    '''
    
    def monitor_shortcut(self):
        
        sc = Shortcut()
        
        camera_key_group = self.rc.config.get('shortcut','camera')
        screen_key_group = self.rc.config.get('shortcut','screen')
        stop_record_key_group = self.rc.config.get('shortcut','stop')
        
        camera_shortcut = [int(key) for key in camera_key_group.split(',')]
        screen_shortcut = [int(key) for key in screen_key_group.split(',')]
        stop_shortcut = [int(key) for key in stop_record_key_group.split(',')]
        
        print('camera shortcut: %s' % camera_shortcut)
        print('screen shortcut: %s' % screen_shortcut)
        print('stop shortcut: %s' % stop_shortcut)
        
        if camera_key_group:
            sc.add(1, camera_shortcut, lambda: self.record(RecordType.Camera))
        if screen_key_group:
            sc.add(2, screen_shortcut, lambda: self.record(RecordType.Screen))
        if stop_record_key_group:
            sc.add(3, stop_shortcut, self.stop_record)
        sc.monitor()
        
    '''
        窗体事件
    '''
    def eventFilter(self, obj, event):
        
        etype=event.type()
        # print('e type: %s' % etype)
        # print('obj is window? %s' % (isinstance(obj,RecordWindow)))
        # print('deactivate type id :%d' % QEvent.WindowDeactivate)
        if etype == QEvent.WindowDeactivate:
            print('丢失焦点')
            #代码功能：当窗口失去焦点（不是键盘事件的焦点），窗体隐藏。
            #引起的问题：当关闭从此窗口弹出的提示框和子窗口时，此窗口异常退出。
            #原因分析：提示框和子窗口在弹出时，引发WindowDeactivate事件主窗口同时隐藏，
            #当提示框和子窗口关闭时，因为父窗口已隐藏子窗口似乎是找不到父窗口，或者猜测是误以为父窗口不存在，然后整个应用随即退出。
            #解决方案1（先用）：用变量need_hide(bool)来控制是否需要隐藏窗体，need_hide=True才隐藏窗体。在打开子窗口和弹出提示窗之前将need_hide=False。
            #缺陷：快捷键操作仍然会有同样的问题，因为窗体大多时候是隐藏的。（考虑：把快捷键监控放在托盘图标上？）
            #更好的解决方案：1.为什么当父窗口是隐藏状态，子窗口关闭，整个应用也随之退出？(关键)
            #2.对窗体事件有更准确的了解，换一种更好的方式来实现窗体失去焦点隐藏主窗体。
            #最终解决方案：1.设置QApplication.setQuitOnLastWindowClosed(False) 
            #2显示逻辑：由此处和RecordTrayIcon.actived事件分别控制，此处负责隐藏；RecordTrayIcon根据此窗体隐藏状态做判断：如果隐藏则显示（即单击或双击显示），
            #如果非隐藏但不是activeWindow，则设置activeWindow=True，否则隐藏。
            
            self.setVisible(False)
            # if self.need_hide:
                # self.setVisible(False)
                # pass
            # else:
                # self.need_hide = True
      
        return False
        
if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    #当这个属性为True，应用程序会在最后一个可见窗口关闭时退出。
    app.setQuitOnLastWindowClosed(False)
    rw = RecordWindow()    
    rw.monitor_shortcut()
    rw.rti.show()
    rw.show()
    sys.exit(app.exec_()) 