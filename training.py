import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn
import numpy as np
import utils_memory as umem
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#sys.setrecursionlimit(100000)
def train_sample(package, size):
        ex1 = codata.get_training_data(package, size)

        #if(len(sys.argv) == 2):
        #    ex1 = codata.get_training_data(sys.argv[1], 11)

        print 'ex1 = '
        print ex1

        # compute delta
        delta = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
        #vector = [0 for i in range(len(ex1)-1)]

        for i in range(0, len(delta)):

            # heap memory increase
            delta[i][0] = (ex1[i+1][0] - ex1[i][0])
            # objects number increase
            delta[i][1] = (ex1[i+1][1] - ex1[i][1])

       # for i in range(0, len(vector)):
       #     if delta[i][1] == 0:
       #         vector[i] = float("inf")
       #     else:
       #         vector[i] = delta[i][0] / delta[i][1]

        print 'delta = ', delta

        delta_mean_matrix = np.mean(delta, axis=0)
        delta_mean = delta_mean_matrix[0]
        print 'delta_mean = ', delta_mean

        total_memory = umem.totalMem1()
        print 'total memory = ' , total_memory

        delta_mean_ratio = delta_mean/int(total_memory)
        print 'delta_mean_ratio = ', delta_mean_ratio * 1000

        delta_heaps = [item[0] for item in delta]
        delta_objects = [item[1] for item in delta]
        #delta_corr_matrix = np.corrcoef(delta_heaps, delta_objects)
        #delta_corr = delta_corr_matrix[0][1]
        #print 'delta_corr = ', delta_corr
        a_heaps = [item[0] for item in ex1]
        a_objects = [item[1] for item in ex1]
        a_corr_matrix = np.corrcoef(a_heaps, a_objects)
        a_corr = a_corr_matrix[0][1]
        print 'a_corr = ', a_corr

        delta_times_ratio = sum([int(item > 0) for item in delta_heaps])/(1.0000 * len(delta_heaps))

        print 'delta_times_ratio = ', delta_times_ratio

       # print 'vector = '
       # print vector
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
       # X = [1, 1, 2, 2]
       # Y = [3, 4, 4, 3]
       # Z = [1, 2, 1, 1]
       # ax.scatter(X, Y, Z)
       #ax.scatter(delta_mean_ratio, delta_corr, delta_times_ratio)
        ax.scatter(delta_mean_ratio, a_corr, delta_times_ratio)
        ax.set_xlabel('delta_mean_ratio')
        ax.set_ylabel('a_corr')
        ax.set_zlabel('delta_times_ratio')
        plt.show()

        drawn.draw_node(delta)
