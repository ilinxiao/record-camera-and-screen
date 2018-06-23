# 获取Windows的已打的补丁号
import winreg
from winreg import *
import re
import os
import datetime
import hashlib

def subRegKey(key, pattern, patchlist):
    # 个数
    count = QueryInfoKey(key)
    for index in range(len(QueryInfoKey(key))):
        # 获取标题
        name = EnumKey(key, index)
        
        result = patch.match(name)
        if result:
            patchlist.append(result.group(1))
        sub = OpenKey(key, name)
        subRegKey(sub, pattern, patchlist)
        CloseKey(sub)

              
def check_run_state():
    #验证运行有效性逻辑：
    #一、判断是否正常安装
    #判断条件：软件安装时在注册表“HKEY_CURRENT_USER\\SOFTWARE\\Gutin\\Record“记录下安装目录
    #二、非正常安装有效时间为三个月,且只能发生一次
    
    #验证当前运行目录是否存在注册表中
    qualified = False
    run_dir = os.path.abspath('.')
    # print('run_dir:%s' % run_dir)
    reg_path = 'SOFTWARE\\Gutin\\Record'
    feature_name ='InstallDir'
    key = OpenKey(HKEY_CURRENT_USER, reg_path, access = KEY_READ)
    items = QueryInfoKey(key)
    for i in range(items[1]):
        item = EnumValue(key, i)
        name = item[0]
        value = item[1]
        type = item[2]
        if name and name.find(feature_name)>=0:
            if os.path.samefile(value, run_dir):
                qualified = True
                break;
    
    if not qualified:
        #查找非正常安装目录记录
        #记录以运行目录的hash值作为键名，值为首次运行的时间
        time_format= '%Y-%m-%d %H:%M:%S'
        run_time = None
        # run_dir_hash = hashlib.md5(run_dir.encode('utf-8')).hexdigest()
        unqualified_key_name  = 'Unqualified'
        has_unqualified = False
        for i in range(items[1]):
            item = EnumValue(key, i)
            name = item[0]
            value = item[1]
            type = item[2]
            if name == unqualified_key_name:
                has_unqualified = True
                run_time = value
      
        if not has_unqualified:
            #如果不存在，创建       
            run_time = datetime.datetime.now().strftime(time_format)
            key = OpenKey(HKEY_CURRENT_USER, reg_path, access = KEY_SET_VALUE)
            SetValueEx(key, unqualified_key_name, 0, REG_SZ, run_time)            
                  
        #判断时限
        # now = datetime.datetime.strptime('2018-06-22 12:11:51', time_format)
        now = datetime.datetime.now()
        run_time_obj = datetime.datetime.strptime(run_time, time_format)
        print('first run_time:%s' % run_time)
        print('now:%s' % now.strftime(time_format))
        
        # qual_days = 1 - (now - run_time_obj).days
        # print('qualified days:%d' % (qual_days))
        print('qualified hours:%d' % (((now - run_time_obj).total_seconds())//3600))
        qual_hours = 18 - ((now - run_time_obj).total_seconds())//3600
        # if qual_days > 0:
        if qual_hours > 0:
            qualified = True
     
    CloseKey(key)
    return qualified
    

if __name__ == '__main__':
    # patchlist = []
    # updates = 'SOFTWARE\\Gutin\\Record'
    # patch = re.compile('InstallDir.+')
    # key = OpenKey(HKEY_CURRENT_USER, updates, access = KEY_READ)
    # items = QueryInfoKey(key)
    # print(items[1])
    # for i in range(items[1]):
        # item = EnumValue(key, i)
        # name = item[0]
        # value = item[1]
        # type = item[2]
        # if name and name.find('InstallDir')>=0:
            # print(item)
            
    print(check_run_state())
            
    # print(items)
    # CloseKey(key) 