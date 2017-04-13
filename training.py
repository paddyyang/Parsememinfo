import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn

ex1 = codata.get_training_data('com.pyzed.androidmemoryleaktest', 11)
print ex1

# compute delta
delta = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]

for i in range(0, len(delta)):
    delta[i][0] = ex1[i+1][0] - ex1[i][0]
    delta[i][1] = ex1[i+1][1] - ex1[i][1]


print delta

drawn.draw_node(delta)
