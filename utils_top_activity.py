import os
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

def topActivity():
    text = execCmd('adb shell dumpsys activity top')
    component = getComponent(text[1])
    return component


test_name = topActivity()
print test_name
