import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn

#sys.setrecursionlimit(100000)
def train_sample(package, size):
        ex1 = codata.get_training_data(package, size)

        #if(len(sys.argv) == 2):
        #    ex1 = codata.get_training_data(sys.argv[1], 11)

        print 'ex1 = '
        print ex1

        # compute delta
        delta = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
        vector = [0 for i in range(len(ex1)-1)]

        for i in range(0, len(delta)):
            delta[i][0] = (ex1[i+1][0] - ex1[i][0])
            delta[i][1] = (ex1[i+1][1] - ex1[i][1])

        for i in range(0, len(vector)):
            if delta[i][1] == 0:
                vector[i] = float("inf")
            else:
                vector[i] = delta[i][0] / delta[i][1]

        print 'delta = '
        print delta

        print 'vector = '
        print vector

        drawn.draw_node(delta)
