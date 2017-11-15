import os
import time
import subprocess
import sys
import math
from enum import Enum

import utils_top_activity as utop
import utils_hiview as uhi
import run_operation as rop

#run a specific test case

loop_index = []

class Color(Enum):
    LOOP = 1
    CURRENT = 2
    CLICK = 3
    ROTATE = 4


def wait_top_activity(activity_name):
   current_activity = utop.topActivity(); 
   i = 0
   while (current_activity != activity_name) and (i < 20):
         time.sleep(5)
         i = i + 1
         current_activity = utop.topActivity(); 
         print 'current_activity: ', current_activity
   return current_activity == activity_name

def assert_top_activity(activity_name):
   current_activity = utop.topActivity(); 
   return current_activity == activity_name;

def execLoop(loop_list):
    #print 'loop_list = ', loop_list, ', len = ' , len(loop_list)
    this_time = loop_list[0]
    print "execLoop time = ", this_time
    i = 0
    temp_index = 0
    lindex = len(loop_index)
    print "lindex = ", lindex
    print "loop_index = ", loop_index
    while i< this_time or this_time == -1:
        j = 1
        wait_once = False
        while j < len(loop_list):
                temp = loop_list[j].strip().split()
                if(lindex > 0):
                    if temp[-1] == "[loopindex]":
                        print "loop_index[temp_index] = ", temp_index, ", ", loop_index[temp_index]
                        temp[-1] = loop_index[temp_index]
                        temp_index = (temp_index + 1) % lindex
                print "j = ", j , ": ", temp
                if temp[0] == "click":
                    rop.tap(temp[1])
                elif temp[0] == "clickxy":
                    rop.clickxy(temp[1], temp[2])
                elif temp[0] == "rotate":
                    rop.rotate(int(temp[1]))
                elif temp[0] == "back":
                    rop.back_key(int(temp[1]))
                elif temp[0] == "cleartext":
                    rop.clear_text(temp[1])
                elif temp[0] == "inputtext":
                    rop.input_text(temp[1], temp[2])
                elif temp[0] == "back_hold":
                    rop.back_hold(int(temp[1]), temp[2])
                elif temp[0] == "current":
                    if assert_top_activity(temp[1]) == False:
                        print "current activity is not the expected: ", temp[1]
                        debug_info()
                        return;
                elif temp[0] == "wait":
                    if wait_top_activity(temp[1]) == False:
                        print "wait activity is failed: ", temp[1]
                        debug_info()
                        if wait_once == False:
                            j = j -1
                            wait_once = True
                            print "set wait_once to True"
                            continue
                        else:
                            rop.killHostPid('python run_test.py')
                            return
                    else:
                        wait_once = False

                j = j + 1
        i = i+1

def execCasePlan(file_name):
        print 'parseCasePlan ', file_name
        f = open(file_name,"r")
        in_loop = False
        loop_list = []
        while True:
            line = f.readline().strip()
            if line:
                if line[0] == '#':
                    continue
                temp = line.split()
                if temp[0] == "startloop":
                    if in_loop == True:
                        print 'error! only support plat loop'
                        debug_info()
                        return
                    in_loop = True
                    loop_time = int(temp[1])
                    loop_list.append(loop_time)
                elif temp[0] == "endloop":
                    if in_loop == False:
                        print 'error! broken loop structure'
                        return
                    in_loop = False
                    execLoop(loop_list)

                elif temp[0] == "current":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        if(assert_top_activity(temp[1]) == False):
                            print "current activity is not the expected: ", temp[1]
                            return
                elif temp[0] == "wait":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        if(wait_top_activity(temp[1]) == False):
                            print "wait activity is failed: ", temp[1]
                            rop.killHostPid('python run_test.py')
                            return
                elif temp[0] == "click":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.tap(temp[1])
                elif temp[0] == "clickxy":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.clickxy(temp[1], temp[2])
                elif temp[0] == "rotate":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.rotate(int(temp[1]))
                elif temp[0] == "back":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.back_key(int(temp[1]))
                elif temp[0] == "cleartext":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.clear_text(temp[1])
                elif temp[0] == "inputtext":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.input_text(temp[1], temp[2])
                elif temp[0] == "back_hold":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.back_hold(int(temp[1]), temp[2])
                elif temp[0] == "loopindex":
                     print "now in loopindex!"
                     i = 1
                     global loop_index
                     loop_index = []
                     while i < len(temp):
                        loop_index.append(temp[i])
                        i = i + 1
                     print "first: loop_index = ", loop_index
            else:
                print temp[0]
                break

        f.close()
        print 'parseCasePlan ', file_name , " OVER!"


def debug_info():
     print "###########################################################"
     print sys._getframe().f_code.co_filename
     print sys._getframe().f_code.co_name
     print sys._getframe().f_lineno
     print "###########################################################"

if(len(sys.argv) >= 2):
    option = sys.argv[1]
    execCasePlan(option)
else:
    print "Usage: run_case file_name"
rop.killHostPid('python run_test.py')
