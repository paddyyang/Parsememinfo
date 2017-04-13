import os
import matplotlib.pyplot as plt
from numpy import *

def draw_node(data_array):
    matrix_data = mat(data_array)
    print 'matrix_data = '
    print matrix_data
    print 'matrix_data[:,0]: '
    print matrix_data[:,0]
    print 'matrix_data[:,1]'
    print matrix_data[:,1]
    a=[0,1, 2, 3]
    b=[4, 5, 6 ,7]
    #plt.scatter(a,b)
    plt.scatter(matrix_data[0,:], matrix_data[1,:])
    plt.show()
