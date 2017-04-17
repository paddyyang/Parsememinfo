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

        print int(size), int(interval), package
        return int(size), int(interval), package
