import os
import time
import subprocess
import sys
import math

import collect_data as codata
import draw_node as drawn
import numpy as np
import pandas as pd
import utils_memory as umem
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#sys.setrecursionlimit(100000)
#def train_sample(package, size):
def train_sample():
        #get all the sub-directory in data directory
        sub_dirs = os.listdir('./data')
        #sub_dirs = [x for x in files if os.path.isdir(x)]
        sub_dirs.sort()
        sub_size = len(sub_dirs)

        data_mat = [[0 for i in range(4)] for j in range(sub_size)]
        data_index = -1

        print 'sub_dirs = ', sub_dirs
        for dir_name in sub_dirs:
                
                leak_memory = 0
                if dir_name.find('noleak') > -1:
                    leak_memory = -1
                elif dir_name.find('leak') > -1:
                    leak_memory = 1


                tmp_index = dir_name.rfind('_')
                package = dir_name[tmp_index+1:]
                print 'package == ', package


                ex1 = codata.get_training_data(package, './data/' + dir_name )

                print 'ex1 = ', ex1

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

                delta_mean_ratio = 1000 * delta_mean/int(total_memory)
                print 'delta_mean_ratio = ', delta_mean_ratio

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

                data_index = data_index + 1
                #format: delta mean ratio, corr, delta times ratio, lean or not, sample label
                data_mat[data_index] = [delta_mean_ratio, a_corr, delta_times_ratio, leak_memory, dir_name]


        print 'data_matrix = ', data_mat


        delta_mean_ratio = [x[0] for x in data_mat]
        a_corr = [x[1] for x in data_mat]
        delta_times_ratio = [x[2] for x in data_mat]
        a_leak_memory = [x[3] for x in data_mat]
        a_dir_name = [x[4] for x in data_mat]

        df = pd.DataFrame()
        df['delta_mean_ratio'] = delta_mean_ratio
        df['a_corr'] = a_corr
        df['delta_times_ratio'] = delta_times_ratio
        df['a_leak_memory'] = a_leak_memory
        df['a_dir_name'] = a_dir_name
        df.to_csv('out.csv', index=False)

#        fig = plt.figure()
#        ax = fig.add_subplot(111, projection='3d')
#        for i in range(0, len(a_leak_memory)):
#            if a_leak_memory[i] == 1:
#                ax.scatter(delta_mean_ratio[i], a_corr[i], delta_times_ratio[i], marker = 'o')
#            elif a_leak_memory[i] == -1:
#                ax.scatter(delta_mean_ratio[i], a_corr[i], delta_times_ratio[i], marker = 'x')
#            else:
#                ax.scatter(delta_mean_ratio[i], a_corr[i], delta_times_ratio[i], marker = '?')
#        ax.set_xlabel('delta_mean_ratio')
#        ax.set_ylabel('a_corr')
#        ax.set_zlabel('delta_times_ratio')
#        plt.show()

        #drawn.draw_node(delta)
