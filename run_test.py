#! /usr/bin/python


import os
import time
import subprocess
import sys
import math

#### self-defined function ###
import collect_data as codata
import parseConfig as pc
import utils_top_activity as utop

def run_monkey_test():
    monkey_cmd = 'adb shell monkey --ignore-crashes --ignore-timeouts --kill-process-after-error  --ignore-security-exceptions --throttle 1000 -v -v -v -s 5 1000 1'
    #os.system(monkey_cmd)
    subprocess.call(monkey_cmd, shell=True)
    print 'run_monkey_test over!'
    return

def generate_logs():
    output_name = time.strftime('%Y-%m-%d-%H-%M-%S.meminfo',time.localtime(time.time()))
    dump_cmd = "adb shell dumpsys meminfo -a | tee ./data/" + output_name
    #subprocess.call(dump_cmd, stdout=subprocess.PIPE, shell=True)
    os.system(dump_cmd)
    print 'collect_memoinfo over!'
    return

def generate_error_log():
    output_name = time.strftime('%Y-%m-%d-%H-%M-%S.meminfo',time.localtime(time.time()))
    dump_cmd = "adb shell logcat -v time -d  | tee ./data/ERROR_" + output_name
    #subprocess.call(dump_cmd, stdout=subprocess.PIPE, shell=True)
    os.system(dump_cmd)
    print 'generate error logcat over!'
    return

def checkExist(package_name):
    current_top = utop.topActivity()
    print "checkExist: package_name: ", package_name, ", current_top: ", current_top 
    return current_top.find(package_name)

print "Usage: \n" + sys.argv[0] + "   <number of times>  <number of interval> or with default config file" 
if(len(sys.argv) == 3):
        interval = int(sys.argv[2])
        times = int(sys.argv[1])
        #ex1 = codata.get_training_data('com.pyzed.androidmemoryleaktest', times)
        #print ex1
else:
        times, interval, package, memory_kb = pc.get_config()

for i in range(0, times):
    if(checkExist(package) > -1):
            generate_logs()
            time.sleep(interval)
    else:
            print "the test package: ", package, " doesn't exist!"
            generate_error_log()
            break


