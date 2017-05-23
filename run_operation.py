import os
import time
import subprocess
import sys
import math

import utils_top_activity as utop
import utils_hiview as uhi

def rotate_screen(orien):
    op_cmd = "./shell/adb_rotate.sh " + orien
    os.system(op_cmd)
    return

def rotate():
    while True:
        rotate_screen('l')
        time.sleep(2);
        rotate_screen('p')

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
   while True:
           l, t = uhi.dumpViewLayout(view_id) 
           op_cmd = "adb shell input tap " + str(l) + ' ' + str(t)
           os.system(op_cmd)
           time.sleep(3);

if(len(sys.argv) >= 2):
    option = sys.argv[1]
    if (option == 'rotate'):
        rotate()
    elif (option == 'restart'):
        restart()
    elif (option == 'tap'):
        tap(sys.argv[2])


