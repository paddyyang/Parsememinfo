import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn
import training
import parseConfig as pc

size, interval, package, memory_kb = pc.get_config()
training.train_sample(package, int(size))
