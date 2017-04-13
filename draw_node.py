import os
import matplotlib.pyplot as plt
from numpy import *

def draw_node(data_array):
    matrix_data = mat(data_array)
    print matrix_data
    plt.scatter(matrix_data[:,0], matrix_data[:,1])
    plt.show()
