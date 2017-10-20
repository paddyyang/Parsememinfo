import os
import time
import subprocess
import sys
import math

import utils_top_activity as utop
import utils_hiview as uhi
import parseConfig as pc

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

def killHostPid(pid_name):
    print 'sys.platform = ', sys.platform, ',' ,pid_name
    if 'darwin' in sys.platform:
            cmd0 = "ps -ef | grep '" + pid_name + "'"
            lines = os.popen(cmd0)
            text = lines.readlines()
            lines.close()

            for str_ps in text:
                if str_ps.find('MacOS') > -1:
                    fields = str_ps.split();
                    cmd0 = "kill -9 " + fields[1]
                    print 'killHostPid cmd is  ', cmd0 
                    os.system(cmd0)

    else: 
            cmd0 = "pidof " + pid_name
            lines = os.popen(cmd0)
            text = lines.readlines()
            lines.close()

            cmd0 = "kill -9 " + text[0]
            os.system(cmd0)

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

def clickxy(x, y):
           op_cmd = "adb shell input tap " + x + ' ' + y
           os.system(op_cmd)
           time.sleep(operation_delay);

def back_key(back_times):
    i = 0
    op_cmd = "adb shell input keyevent BACK"
    while i < int(back_times):
           os.system(op_cmd)
           time.sleep(operation_delay);
           i = i + 1

def menu_key(back_times):
    i = 0
    op_cmd = "adb shell input keyevent MENU"
    while i < int(back_times):
           os.system(op_cmd)
           time.sleep(operation_delay);
           i = i + 1
def home_key(back_times):
    i = 0
    op_cmd = "adb shell input keyevent HOME"
    while i < int(back_times):
           os.system(op_cmd)
           time.sleep(operation_delay);
           i = i + 1
        
def back_hold(back_times, hold_activity):
    i = 0
    op_cmd = "adb shell input keyevent BACK"
    loop_inf = False

    if back_times == -1:
        loop_inf = True
    while (i < int(back_times)) or loop_inf:
           top_component = utop.topActivity() 
           if top_component == hold_activity :
                break
           os.system(op_cmd)
           time.sleep(operation_delay);
           i = i + 1

def run_monkey_test():
    times, interval, package_name, memory_kb = pc.get_config()
    if(package_name != ''): 
        monkey_cmd = "adb shell monkey -p " +  package_name + " --ignore-crashes --ignore-timeouts --kill-process-after-error  --ignore-security-exceptions --throttle 2000 --pct-touch 70 --pct-syskeys 20 --pct-anyevent 10 -v -v -v -s 5 100000000 100000000"
        print 'monkey_cmd =', monkey_cmd
    else:
        monkey_cmd = 'adb shell monkey --ignore-crashes --ignore-timeouts --kill-process-after-error  --ignore-security-exceptions --throttle 1000 --pct-touch 70 --pct-syskeys 20 --pct-anyevent 10 -v -v -v -s 5 1000 1000'

    #os.system(monkey_cmd)
    subprocess.call(monkey_cmd, shell=True)
    print 'run_monkey_test over!'
    return

#if(len(sys.argv) >= 2):
#    option = sys.argv[1]
#    if (option == 'rotate'):
#        rotate()
#    elif (option == 'restart'):
#        restart()
#    elif (option == 'tap'):
#        tap(sys.argv[2])
#    elif (option == 'monkey'):
#        run_monkey_test()
#    else:
#        killHostPid('Python run_test.py')
#

