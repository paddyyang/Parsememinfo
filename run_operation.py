import os
import time
import subprocess
import sys
import math

def rotate_screen(orien):
    op_cmd = "./shell/adb_rotate.sh " + orien
    os.system(op_cmd)
    return


while True:
   rotate_screen('l')
   time.sleep(2);
   rotate_screen('p')
