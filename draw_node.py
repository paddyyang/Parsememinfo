import os
import matplotlib.pyplot as plt
#from numpy import *
import numpy as np

def draw_node(data_array):
    #matrix_data = mat(data_array)
    a=[x[0] for x in data_array]
    b=[y[1] for y in data_array]
    plt.scatter(a, b)
    plt.show()
