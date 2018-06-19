import sys,os
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import RecordType
from RecordType import *

class RecordTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(RecordTrayIcon, self).__init__(parent)
        # print((p_menu.actions()))
        # self.showAction1 = QAction("显示消息1", self, triggered=self.showM)
        # print(type(self.parent))
        # p_menu.insertAction(p_menu.actions()[len(p_menu.actions())-1], self.showAction1)       
        
        # self.showMenu()
        self.createContextMenu(parent)
        self.interactive()
        # self.update_state(False,None)
 
        
    def createContextMenu(self, parent):   
        p_menu = parent.contextMenu
        self.setContextMenu(p_menu)

    def interactive(self):
        self.activated.connect(self.iconClicked)           
        self.toolTip()

    def showMessage():
        pass
          
    def get_icon(self, file_name):
    
        data_dir=''
        
        if getattr(sys, 'frozen', False):
            # The application is frozen
            data_dir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            data_dir = os.path.dirname(__file__)
            
        resource_dir = 'resource'
        data_dir = os.path.join(os.path.abspath(data_dir), resource_dir)
        print('resource dir: %s' % data_dir)
            
        icon_file_path = os.path.join(data_dir, file_name)
        if os.path.isfile(icon_file_path):
            return QIcon(icon_file_path)
        return None

    def update_state(self, recording, record_type):
        
        if recording:
            if record_type == RecordType.Camera:
                self.setIcon(self.get_icon('camera_recording_colorful.png'))
                self.setToolTip('正在录制摄像头...')
                
            elif record_type == RecordType.Screen:
                self.setIcon(self.get_icon('screen_recording.png'))
                self.setToolTip('正在录制屏幕...')
            else:
                self.setIcon(self.get_icon('stop.png'))
                self.setToolTip('软件缩小在这里.')
        else:
            self.setIcon(self.get_icon('start.png'))
            self.setToolTip('软件缩小在这里.')
            
        
    def iconClicked(self, reason):
        #"鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            print('clicked.')
            pw = self.parent()
            # print('trayicon is activateWindow?:%s' % self.isActiveWindow())
            if pw.isVisible(): #and pw.isActiveWindow()
                # print('pw is active?%s' % pw.isActiveWindow())
                if not pw.isActiveWindow():
                    pw.activateWindow()
                    # pw.raise_()
                else:
                    pw.hide()
                # pw.hide()
                pass
            else:
                pw.show()
                # pw.raise_()
                pw.activateWindow()
            # print('parent is active window? %s' % pw.isActiveWindow())
        # print(reason)