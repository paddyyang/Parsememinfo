import os
import time
import subprocess
import sys
import math

import utils_top_activity as utop
import utils_hiview as uhi

#delay for 3 second
operation_delay = 1

def rotate_screen(orien):
    op_cmd = "./shell/adb_rotate.sh " + orien
    os.system(op_cmd)
    return

#if loop_time == -1, loop froever
def rotate(loop_time):
    print "rotate time: ", loop_time
    if loop_time == -1:
            while True:
                rotate_screen('l')
                time.sleep(operation_delay);
                rotate_screen('p')
    else:
            i = 0
            while True:
                rotate_screen('l')
                time.sleep(operation_delay)
                rotate_screen('p')
                print "i = ", i, 'loop_time = ', loop_time
                if int(i) == int(loop_time):
                    break
                i = i + 1

def killPackage(package):
    op_cmd = "adb shell am force-stop " + package
    os.system(op_cmd)
    return

def startPackage(component):
    op_cmd = "adb shell am start -n " + component
    os.system(op_cmd)
    return
    
def restart():
    component = utop.topActivity() 
    temp = component.split('/')
    package = temp[0]
    while True:
       killPackage(package)
       time.sleep(3);
       startPackage(component) 
       time.sleep(3);

def tap(view_id):
   #while True:
           l, t = uhi.dumpViewLayout(view_id) 
           op_cmd = "adb shell input tap " + str(l) + ' ' + str(t)
           os.system(op_cmd)
           time.sleep(operation_delay);

def back_key(back_times):
    i = 0
    op_cmd = "adb shell input keyevent BACK"
    while i < int(back_times):
           os.system(op_cmd)
           time.sleep(operation_delay);
           i = i + 1
        

if(len(sys.argv) >= 2):
    option = sys.argv[1]
    if (option == 'rotate'):
        rotate()
    elif (option == 'restart'):
        restart()
    elif (option == 'tap'):
        tap(sys.argv[2])


