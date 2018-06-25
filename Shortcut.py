import PyHook3
import pythoncom

class Shortcut():
    
    global HOTKEYS
    global ACTIONS
    global KEY_STATUS
    global PRESSED_COUNT
    
    HOTKEYS = {}
    ACTIONS = {}
    KEY_STATUS = {}
    PRESSED_COUNT = {}
    
    def __init__(self):
        pass
        
    def add(self, key_group_id , key_group, action):    
        global HOTKEYS
        global ACTIONS
        
        HOTKEYS[key_group_id] = key_group
        ACTIONS[key_group_id] = action
        
    def clear(self):
        HOTKEYS.clear()
        ACTIONS.clear()

    def KeyDownEvent(self, event):
        global KEY_STATUS
        global HOTKEYS
        global PRESSED_COUNT
        global ACTIONS
        
        #标记状态
        KEY_STATUS[event.KeyID] = True
        # print('HOTKEYS: \n%s' % HOTKEYS)
        # print('KEY DOWN/press key status: \n %s' % KEY_STATUS)
        
        for action_id, key_group in HOTKEYS.items():
            #检查每个按键状态
            pressed = True
            for i in range(len(key_group)):
                key = key_group[i]
                if key not in KEY_STATUS:
                    pressed = False
                    break
            
            if pressed:
                # if action_id not in PRESSED_COUNT.keys():
                    # PRESSED_COUNT[action_id] =1
                # else:
                    # PRESSED_COUNT[action_id] +=1
                print('match.')  
                #限制一直按下快捷键 动作执行的次数
                if action_id not in PRESSED_COUNT.keys():    
                    action=ACTIONS[action_id]
                    if action:
                        action()
                    PRESSED_COUNT[action_id] =1
                
        
        
        return True

    def KeyUpEvent(self, event):
        global KEY_STATUS
        global HOTKEYS
        global PRESSED_COUNT
        global ACTIONS

        if event.KeyID in KEY_STATUS.keys():
            KEY_STATUS.pop(event.KeyID)
        # print('KEY UP/press key status: \n %s' % KEY_STATUS)
        
        #清空组合按键记录
        for action_id, key_group in HOTKEYS.items():
            if event.KeyID in key_group:
                if action_id in PRESSED_COUNT.keys():
                    PRESSED_COUNT.pop(action_id)
                    
        return True
        
    def monitor(self):
    
        # create the hook mananger
        hm = PyHook3.HookManager()
        # hm.MouseAllButtonsDown = OnMouseEvent
        hm.KeyDown = self.KeyDownEvent
        hm.KeyUp = self.KeyUpEvent
        
        hm.HookKeyboard()
        # pythoncom.PumpMessages()
    
