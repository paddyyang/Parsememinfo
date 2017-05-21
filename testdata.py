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

def show_data():
    df = pd.read_csv('out.csv')
    delta_mean_ratio = df['inc_memory_ratio']
    a_corr = df['a_corr']
    delta_times_ratio = df['delta_times_ratio']
    a_leak_memory =  df['a_leak_memory']
    a_dir_name = df['a_dir_name']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(0, len(a_leak_memory)):
        if a_leak_memory[i] == 1:
            ax.scatter(delta_mean_ratio[i], a_corr[i], delta_times_ratio[i], marker = 'o')
        elif a_leak_memory[i] == -1:
            ax.scatter(delta_mean_ratio[i], a_corr[i], delta_times_ratio[i], marker = 'x')
        else:
            ax.scatter(delta_mean_ratio[i], a_corr[i], delta_times_ratio[i], marker = '?')

    ax.set_xlabel('inc_memory_ratio')
    ax.set_ylabel('a_corr')
    ax.set_zlabel('delta_times_ratio')
    plt.show()


show_data()
