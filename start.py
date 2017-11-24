import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn
import training
import parseConfig as pc

#size, interval, package, memory_kb = pc.get_config()
#training.train_sample(package, int(size))
if len(sys.argv) > 2:
    training.train_sample(sys.argv[1], sys.argv[2])
elif len(sys.argv) > 1:
    training.train_sample(sys.argv[1])
else:
    training.train_sample('')
