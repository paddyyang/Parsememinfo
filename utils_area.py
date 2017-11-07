import os
import math

#
#  use 'adb shell dumpsys activity top' command
#  will give us the current activity name
#

def compute(a, b):
    if a * b < 0:
        h1 = 1.0 * abs(a)/(abs(a) + abs(b))
        h2 = 1.0 * abs(b)/(abs(a) + abs(b))
        area = a*h1/2.0 + b*h2/2.0 
        return area
    else:
        area = (a + b) * 1 / 2.0
        return area

def compute_all(a, b):
    if a * b < 0:
        h1 = 1.0 * abs(a)/(abs(a) + abs(b))
        h2 = 1.0 * abs(b)/(abs(a) + abs(b))
        area = abs(a)*h1/2.0 + abs(b)*h2/2.0 
        return area
    else:
        area = (abs(a) + abs(b)) * 1 / 2.0
        return area

def compute_delta(ex1):
                data_array = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
                for i in range(0, len(data_array)):
                    # heap memory increase
                    data_array[i][0] = (ex1[i+1][0] - ex1[i][0])
                    # objects number increase
                    data_array[i][1] = (ex1[i+1][1] - ex1[i][1])
                return data_array

def compute_sign(value):
    if value < 0:
        return -1.0
    else:
        return 1.0

def compute_entropy(ex1):
                data_array = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
                entropy_array = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
                entropy_sum = [0 for i in range(len(ex1[0]))]
                for i in range(0, len(data_array)):
                    data_array[i][0] = (ex1[i+1][0] - ex1[i][0])
                    #data_array[i][1] = (ex1[i+1][1] - ex1[i][1])
                 
                for i in range(0, len(data_array)):
                    entropy_sum[0] = entropy_sum[0] + abs(data_array[i][0])
                    #entropy_sum[1] = entropy_sum[1] + abs(data_array[i][1])

                for i in range(0, len(entropy_array)):
                    if data_array[i][0] == 0:
                        entropy_array[i][0]  = 0.0
                    else:
                        entropy_array[i][0] = -1.0*math.log(1.0 * abs(data_array[i][0])/entropy_sum[0], 2) * \
                                                                            compute_sign(data_array[i][0])
                    #entropy_array[i][1] = -1.0*math.log(1.0 * abs(data_array[i][1])/entropy_sum[1], 2) 

                print "entropy_array: ", entropy_array

                #for i in range(0, len(entropy_array)):
                #    entropy_array[i][0] =  entropy_array[i][0] * data_array[i][0] 
                #    entropy_array[i][1] =  entropy_array[i][1] * data_array[i][1] 


                return entropy_array
                
def compute_array(ex1):
                #now we compute memory area for increase or decrease
                inc_area = 0.0
                total_area = 0.0

                #data_array = [[0.0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
                #for i in range(0, len(data_array)):
                #    # heap memory increase
                #    data_array[i][0] = (ex1[i+1][0] - ex1[i][0])
                #    # objects number increase
                #    data_array[i][1] = (ex1[i+1][1] - ex1[i][1])
                data_array = compute_entropy(ex1)

                for i in range(0, len(data_array)):
                    if i == 0:
                        inc_area = inc_area + compute(0, data_array[i][0])
                        total_area = total_area + compute_all(0, data_array[i][0])
                    else:
                        inc_area = inc_area + compute(data_array[i-1][0], data_array[i][0])
                        total_area = total_area + compute_all(data_array[i-1][0], data_array[i][0])
                        
                inc_memory_ratio = inc_area / total_area
                print 'inc_memory_ratio = ', inc_memory_ratio
                return inc_memory_ratio

# test
area1 = compute(3, 4)
print 'area1 = ', area1
area2 = compute(3, -3)
print 'area2 = ', area2
area3 = compute(3, 3)
print 'area3 = ', area3

a1=[[1,0], [2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[100,0],[9,0]]
compute_array(a1)
