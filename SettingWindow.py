from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import DevicesInfo
from DevicesInfo import *
import RecordConfig
from RecordConfig import *
from PyQt5.QtWidgets import QMessageBox
import resource
import psutil

class SettingWindow(QDialog):
    
    
    update_setting = pyqtSignal(bool)
    def __init__(self, parent = None):
        super(SettingWindow,self).__init__(parent)
        
        self.changed = False
        self.setupUi()
        self.load()

    def setupUi(self):
        self.setObjectName("SettingWindow")
        self.setFixedSize(383, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/gutin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 371, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_device = QtWidgets.QWidget()
        self.tab_device.setObjectName("tab_device")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_device)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.cb_camera_devices = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cb_camera_devices.setObjectName("devices.camera_device_name")
        self.gridLayout_3.addWidget(self.cb_camera_devices, 0, 1, 1, 1)
        self.cb_voice_devices = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cb_voice_devices.setObjectName("devices.voice_device_name")
        self.gridLayout_3.addWidget(self.cb_voice_devices, 1, 1, 1, 1)
        self.cb_screen_devices = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cb_screen_devices.setObjectName("devices.screen_device_name")
        self.gridLayout_3.addWidget(self.cb_screen_devices, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.cb_system_voice_devices = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cb_system_voice_devices.setObjectName("devices.system_voice_device_name")
        self.gridLayout_3.addWidget(self.cb_system_voice_devices, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_device, "")
        self.tab_key = QtWidgets.QWidget()
        self.tab_key.setObjectName("tab_key")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_key)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.le_start_record_screen_shortcut = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_start_record_screen_shortcut.setObjectName("shortcut.screen")
        self.gridLayout_2.addWidget(self.le_start_record_screen_shortcut, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.le_start_record_camera_shortcut = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_start_record_camera_shortcut.setObjectName("shortcut.camera")
        self.gridLayout_2.addWidget(self.le_start_record_camera_shortcut, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.le_start_stop_exit_shortcut = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_start_stop_exit_shortcut.setObjectName("shortcut.stop")
        self.gridLayout_2.addWidget(self.le_start_stop_exit_shortcut, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_key, "")
        self.tab_record = QtWidgets.QWidget()
        self.tab_record.setObjectName("tab_record")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_record)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.cb_resolution = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb_resolution.setObjectName("record.resolution")
        self.gridLayout.addWidget(self.cb_resolution, 0, 1, 1, 1)
        self.cb_vcodec = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb_vcodec.setObjectName("record.vcodec")
        self.gridLayout.addWidget(self.cb_vcodec, 1, 1, 1, 1)
        self.dsb_frame_rate = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_frame_rate.sizePolicy().hasHeightForWidth())
        self.dsb_frame_rate.setSizePolicy(sizePolicy)
        self.dsb_frame_rate.setObjectName("record.frame_rate")
        self.gridLayout.addWidget(self.dsb_frame_rate, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.le_file_path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_file_path.sizePolicy().hasHeightForWidth())
        self.le_file_path.setSizePolicy(sizePolicy)
        self.le_file_path.setObjectName("record.file_dir")
        self.gridLayout.addWidget(self.le_file_path, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.btn_file_dir = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_file_dir.sizePolicy().hasHeightForWidth())
        self.btn_file_dir.setSizePolicy(sizePolicy)
        self.btn_file_dir.setObjectName("btn_file_dir")
        self.gridLayout.addWidget(self.btn_file_dir, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab_record, "")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 330, 229, 10))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.threads_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.threads_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.threads_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.threads_label.setObjectName("threads_label")
        self.gridLayout.addWidget(self.threads_label, 5, 0, 1, 1)
        self.threads_spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threads_spinBox.sizePolicy().hasHeightForWidth())
        self.threads_spinBox.setSizePolicy(sizePolicy)
        self.threads_spinBox.setObjectName("record.threads")
        self.gridLayout.addWidget(self.threads_spinBox, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_record, "")
        
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setGeometry(QtCore.QRect(180, 240, 75, 23))
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(self)
        self.cancel_button.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "设置"))
        self.label_3.setText(_translate("Form", "屏幕录制设备："))
        self.label_2.setText(_translate("Form", "声音输入设备："))
        self.label.setText(_translate("Form", "摄像头名称："))
        self.label_4.setText(_translate("Form", "系统声音设备："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_device), _translate("Form", "设备参数配置"))
        self.label_10.setText(_translate("Form", "录制屏幕："))
        self.label_9.setText(_translate("Form", "录制摄像头："))
        self.label_11.setText(_translate("Form", "启动/退出："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_key), _translate("Form", "快捷键设置"))
        self.label_14.setText(_translate("Form", "编码格式："))
        self.label_15.setText(_translate("Form", "帧率："))
        self.label_13.setText(_translate("Form", "文件保存目录："))
        self.label_12.setText(_translate("Form", "分辨率："))
        self.btn_file_dir.setText(_translate("Form", "选择文件目录"))
        self.threads_label.setText(_translate("Form", "CPU线程："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_record), _translate("Form", "录制参数"))
        self.save_button.setText(_translate("Form", "保存"))
        self.cancel_button.setText(_translate("Form", "取消"))
        
    def load_combobox_data(self, combox, data):
        #下拉列表数据加载
        for obj in data:
            name = obj[0]
            value = name 
            if len(obj) > 1:
                value = obj[1]
            combox.addItem(name, value)
    
    def get_key_group_name(self, key_tuple):
        return key_tuple.replace(r'(','').replace(r')','')
     
    def load_config(self):
        '''
            加载设置         
        '''  
        #设备
        video_device_name = self.rc.config.get('devices','camera_device_name')
        voice_device_name = self.rc.config.get('devices','voice_device_name')
        screen_device_name = self.rc.config.get('devices','screen_device_name')
        system_voice_device_name = self.rc.config.get('devices','system_voice_device_name')
        
        # self.cb_camera_devices.setCurrentIndex(1)
        video_cur_index = self.cb_camera_devices.findData(video_device_name)
        # print('video name:\n%s\ndevice index:%d' % (video_device_name, video_cur_index))
        self.cb_camera_devices.setCurrentIndex(video_cur_index)
        
        self.cb_voice_devices.setCurrentIndex(self.cb_voice_devices.findData(voice_device_name))
        self.cb_screen_devices.setCurrentIndex(self.cb_screen_devices.findData(screen_device_name))
        self.cb_system_voice_devices.setCurrentIndex(self.cb_system_voice_devices.findData(system_voice_device_name))
        
        #快捷键
        record_camera_key_group = self.rc.config.get('shortcut','camera')
        record_screen_key_group = self.rc.config.get('shortcut','screen')
        record_stop_key_group = self.rc.config.get('shortcut','stop')
        
        record_camera_key_group_name = self.get_key_group_name(record_camera_key_group)
        record_screen_key_group_name = self.get_key_group_name(record_screen_key_group)
        record_stop_key_group_name = self.get_key_group_name(record_stop_key_group)
        
        self.le_start_record_camera_shortcut.setText(record_camera_key_group_name)
        self.le_start_record_screen_shortcut.setText(record_screen_key_group_name)
        self.le_start_stop_exit_shortcut.setText(record_stop_key_group_name)
        
        #录制参数
        record_resolution = self.rc.config.get('record','resolution')
        record_vcodec = self.rc.config.get('record','vcodec')
        record_frame_rate = self.rc.config.getfloat('record','frame_rate')
        record_file_dir = self.rc.config.get('record','file_dir')
        record_file_dir = os.path.abspath(record_file_dir)
        record_threads = int(self.rc.config.get('record','threads'))
        
        self.cb_resolution.setCurrentIndex(self.cb_resolution.findData(record_resolution))
        self.cb_vcodec.setCurrentIndex(self.cb_vcodec.findData(record_vcodec))
        self.dsb_frame_rate.setValue(record_frame_rate)
        self.le_file_path.setText(record_file_dir)
        
        self.threads_spinBox.setValue(record_threads)
     
    def load(self):
        
        self.rc = RecordConfig()
        '''
            数据初始化
        '''
        #设备
        di = DevicesInfo()
        self.load_combobox_data(self.cb_camera_devices, di.video_devices)
        self.load_combobox_data(self.cb_screen_devices, di.video_devices)
        self.load_combobox_data(self.cb_voice_devices, di.voice_devices)
        self.load_combobox_data(self.cb_system_voice_devices, di.voice_devices)
        
        #录制
        resolutions = [
            ['1920x1080'],
            ['1280x1024'],
            ['1024x768'],
            ['640x480']
        ]
        
        vcodec = [
        ['H.264','libx264'],
        ['H.265','libx265'],
        ]
        self.load_combobox_data(self.cb_resolution, resolutions)
        self.load_combobox_data(self.cb_vcodec, vcodec)
        
        self.dsb_frame_rate.setDecimals(1)
        cpu_count = psutil.cpu_count(logical=True)
        self.threads_spinBox.setMaximum(cpu_count)
        
        # print(self.cb_camera_devices.currentData())
        # print('视频设备列表:')
        # print(di.video_devices)
        # print('音频设备列表:')
        # print(di.voice_devices)
        
        self.load_config()
        
        '''
            关联事件
        '''
        #设备
        self.cb_camera_devices.currentIndexChanged.connect(self.stateChangedEvent)
        self.cb_voice_devices.currentIndexChanged.connect(self.stateChangedEvent)
        self.cb_screen_devices.currentIndexChanged.connect(self.stateChangedEvent)
        self.cb_system_voice_devices.currentIndexChanged.connect(self.stateChangedEvent)
        
        #快捷键
        self.le_start_record_camera_shortcut.textChanged.connect(self.stateChangedEvent)
        self.le_start_record_screen_shortcut.textChanged.connect(self.stateChangedEvent)
        self.le_start_stop_exit_shortcut.textChanged.connect(self.stateChangedEvent)
        
        #录制参数
        self.cb_resolution.currentIndexChanged.connect(self.stateChangedEvent)
        self.cb_vcodec.currentIndexChanged.connect(self.stateChangedEvent)
        self.dsb_frame_rate.valueChanged.connect(self.stateChangedEvent)
        self.le_file_path.textChanged.connect(self.stateChangedEvent)
        self.threads_spinBox.valueChanged.connect(self.stateChangedEvent)
            
        # self.le_start_record_camera_shortcut.keyPressEvent = self.record_keypress
        # print(dir(self.le_start_record_camera_shortcut.keyPressEvent))
        
        
        # self.le_file_path.setText()
        self.btn_file_dir.clicked.connect(self.file_dir_select)
        self.save_button.clicked.connect(self.save_setting)
        self.cancel_button.clicked.connect(self.cancel)
        
        self.update_state()
        
    
    def record_keypress(self, event):
        print('text:%s' %event.text())
        print('key:%d' % event.key())
        print('modifiers: %s' % event.modifiers())
        print('nativeVirtualKey:%s' % event.nativeVirtualKey())
        
    def file_dir_select(self, event):
        current_dir = self.le_file_path.text()
        # print('current dir:%s' % current_dir)
        if not os.path.exists(current_dir):
            current_dir = os.path.abspath('.')
        selected_dir = QFileDialog.getExistingDirectory(self, '选择录像保存目录', current_dir, QFileDialog.ShowDirsOnly)
        if selected_dir and os.path.exists(selected_dir):
            self.le_file_path.setText(selected_dir)
        
    def showSettingWindow(self):
        if not self.isVisible():
            self.exec_()
        
    def closeEvent(self, event):
        print('changed?%s' % self.changed)
        if self.changed:
            
            self.save_setting()
            
            question = QMessageBox(self)
            question.setText('设置已保存，重新启动软件生效。')
            question.setWindowTitle('提示')
            question.setIcon(QMessageBox.Question)
            question.addButton(QMessageBox.Yes)
            question.exec()
            print('parent is None?%s' % (self.parent is None))
            self.changed = False
            
        # self.setVisible(False)
        # event.ignore()
    
    def save_setting(self):
        
        
        #获取改动值
        #设备
        camera_device_name = self.cb_camera_devices.currentData()
        voice_device_name = self.cb_voice_devices.currentData()
        screen_device_name = self.cb_screen_devices.currentData()
        system_voice_device_name = self.cb_system_voice_devices.currentData()
        # print(camera_device_name)
        
        #快捷键
        record_camera_key_group_name = self.le_start_record_camera_shortcut.text()
        record_screen_key_group_name = self.le_start_record_screen_shortcut.text()
        record_stop_key_group_name = self.le_start_stop_exit_shortcut.text()
        # print(record_camera_key_group_name)
        
        #录制
        resolution = self.cb_resolution.currentData()
        video_codec = self.cb_vcodec.currentData()
        frame_rate = self.dsb_frame_rate.value()
        file_dir = self.le_file_path.text()
        threads = self.threads_spinBox.value()
        # print(threads)
        
        #保存
        conf = self.rc.config
        
        devices_section_name = 'devices'    
        conf.set(devices_section_name,'camera_device_name', camera_device_name)
        conf.set(devices_section_name,'voice_device_name', voice_device_name)
        conf.set(devices_section_name,'screen_device_name', screen_device_name)
        conf.set(devices_section_name,'system_voice_device_name', system_voice_device_name)
        
        shortcut_section_name = 'shortcut'
        conf.set(shortcut_section_name,'camera', record_camera_key_group_name)
        conf.set(shortcut_section_name,'screen', record_screen_key_group_name)
        conf.set(shortcut_section_name,'stop', record_stop_key_group_name)
        
        record_section_name = 'record'
        conf.set(record_section_name,'resolution', resolution)
        conf.set(record_section_name,'vcodec', video_codec)
        conf.set(record_section_name,'frame_rate', str(frame_rate))
        conf.set(record_section_name,'file_dir', file_dir)
        conf.set(record_section_name,'threads', str(threads))
        
        self.rc.write()
        #通知主窗口更新设置
        self.update_setting.emit(self.changed)
        self.changed = False
        self.update_state()
    
    def update_state(self):
    
        self.save_button.setDisabled(not self.changed)
        self.cancel_button.setDisabled(not self.changed)
        
    def cancel(self):
        self.load_config()
        self.changed=False
        self.update_state()
        
    def setting(self, obj_name, value):
        
        section = ''
        name = ''
        if obj_name.find('.') >= 0:
            section = obj_name.split('.')[0]
            name = obj_name.split('.')[1]
            if type(value) == type(''):
                value = value.strip()
            print('check param in index changed:')
            print('section:%s' % section)
            print('name:%s' % name )
            print('value:%s' % value)
            
        if self.rc.config.has_option(section, name):
           
            self.changed = True
            self.rc.config.set(section, name, value)
        else:
            pass
            print('not found this section or name.')
        
    # def indexChangedEvent(self, index, obj):
        
        # print('in data changed event.')
        # print(index)
        # print('event obj:%s' % type(obj))
        # print('obj name:%s' % obj.objectName())
        
        # value = obj.currentData()
        # obj_name = obj.objectName()
        # self.setting(obj_name, value)
    def stateChangedEvent(self, new_value):
        print('changed value is :%s' % new_value)
        self.changed = True
        self.update_state()
        
    # def textChangedEvent(self, obj):
    
        # print('type of self:%s' % type(self))
        # print('type of text:%s' % type(text))
        # print('type of obj:%s' % type(obj))
        # value = obj.text()
        # obj_name = obj.objectName()
        # self.setting(obj_name, value)
        
    # def valueChangedEvent(self, new_value):
        # print('changed  value is :%s.' % new_value)
        
        # self.changed = True
        # self.update_state()
        # obj = self.dsb_frame_rate
        # value = obj.value()
        # print('value:%1.f' % value)
        # obj_name = obj.objectName()
        # self.setting(obj_name, str(value))
        
    # def valueChangedEvent_spinBox(self):
        # print('in value changed event.')
        # obj = self.threads_spinBox
        # value = obj.value()
        # print('value:%1.f' % value)
        # obj_name = obj.objectName()
        # self.setting(obj_name, str(value))
        

