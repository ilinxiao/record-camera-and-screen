import os,configparser
# import DevicesInfo
# from DevicesInfo import *

class RecordConfig():
    def __init__(self, config_file_name = 'configByLinxiao.ini'):
        self.file_name = config_file_name
        self.encoding = 'gb2312'
        self.load()

    def load(self):
    
        if os.path.exists(self.file_name):
            self.config=configparser.SafeConfigParser()
            self.config.read(self.file_name, encoding = self.encoding)
        else:
            self.write_default_config()
            self.load()
            
    def write_default_config(self):
        print('初始化配置文件.')
        conf = configparser.SafeConfigParser()
        
        # di = DevicesInfo()
        devices_section_name = 'devices'       
        conf.add_section(devices_section_name)
        conf.set(devices_section_name,'camera_device_name','')
        conf.set(devices_section_name,'voice_device_name','')
        conf.set(devices_section_name,'screen_device_name','')
        conf.set(devices_section_name,'system_voice_device_name','')
        
        shortcut_section_name = 'shortcut'
        conf.add_section(shortcut_section_name)
        conf.set(shortcut_section_name,'camera','160,162,164,65')
        conf.set(shortcut_section_name,'screen','160,162,164,66')
        conf.set(shortcut_section_name,'stop','160,162,164,67')
        
        record_section_name = 'record'
        conf.add_section(record_section_name)
        conf.set(record_section_name,'resolution','1920x1080')
        conf.set(record_section_name,'adaptive_screen_resolution','1')
        conf.set(record_section_name,'vcodec','libx264')
        conf.set(record_section_name,'frame_rate','7.0')
        conf.set(record_section_name,'file_dir','.')
        conf.set(record_section_name,'threads', '4')
        
        conf.add_section('author')
        conf.set('author', 'name', 'linxiao')
        conf.set('author', 'mail', '940950943@qqqqqqqqqqqqqqqqqqqqqqqqqqqq.com')
        
        self.config = conf
        self.write()
        
    def write(self):
        with open(self.file_name, 'wt', encoding = self.encoding) as configfp:
            self.config.write(configfp)
       
        