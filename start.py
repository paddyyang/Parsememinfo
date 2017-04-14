import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn

import ConfigParser as conp

config = conp.ConfigParser()
config.read('sample.config')
size = config.get('settings', 'size')
interval = config.get('settings', 'interval')
package = config.get('settings', 'package')
print size, interval, package
