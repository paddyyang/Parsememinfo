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

class Color(Enum):
    LOOP = 1
    CURRENT = 2
    CLICK = 3
    ROTATE = 4


#if(len(sys.argv) >= 2):
#    option = sys.argv[1]
#    if (option == 'rotate'):
#        rotate()
#    elif (option == 'restart'):
#        restart()
#    elif (option == 'tap'):
#        tap(sys.argv[2])
#

def assert_top_activity(activity_name):
   current_activity = utop.topActivity(); 
   return current_activity == activity_name;

def execLoop(loop_list):
    #print 'loop_list = ', loop_list, ', len = ' , len(loop_list)
    this_time = loop_list[0]
    print "execLoop time = ", this_time
    i = 0
    while i< this_time:
        j = 1
        while j < len(loop_list):
                temp = loop_list[j].strip().split()
                print "j = ", j , ": ", temp
                if temp[0] == "click":
                    rop.tap(temp[1])
                elif temp[0] == "rotate":
                    rop.rotate(int(temp[1]))
                elif temp[0] == "back":
                    rop.back_key(int(temp[1]))
                elif temp[0] == "current":
                    if assert_top_activity(temp[1]) == False:
                        print "current activity is not the expected: ", temp[1]
                        debug_info()
                        return;
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
                elif temp[0] == "click":
                    if in_loop == True:
                        loop_list.append(line.strip())
                    else:
                        rop.tap(temp[1])
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

            else:
                break

        f.close()
        print 'parseCasePlan ', file_name , " OVER!"


def debug_info():
     print "###########################################################"
     print sys._getframe().f_code.co_filename
     print sys._getframe().f_code.co_name
     print sys._getframe().f_lineno
     print "###########################################################"

execCasePlan('case0.txt')