import os
import time
import subprocess
import sys
import math
import ConfigParser as conp

def get_config():
        config = conp.ConfigParser()
        config.read('sample.config')
        size = config.get('settings', 'size')
        interval = config.get('settings', 'interval')
        package = config.get('settings', 'package')
        memory_kb = config.get('settings', 'memory_kb')

        print int(size), int(interval), package, memory_kb
        return int(size), int(interval), package, int(memory_kb)
