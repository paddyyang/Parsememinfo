import os
import parseConfig as pc

#
#  use 'adb shell dumpsys activity top' command
#  will give us the current activity name
#
def execCmd(cmd):
    lines = os.popen(cmd)
    text = lines.readlines()
    lines.close()
    return text

def getComponent(line_text):
    
     line0 = line_text.strip()
     if line0:
        temp = line0.split()

     return temp[1]

def totalMem():
    text = execCmd('adb shell cat /proc/meminfo')
    component = getComponent(text[0])
    return component

def totalMem1():
    size, interval, package, memory_kb = pc.get_config()
    return memory_kb
