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
                entropy_array_value = [[0 for i in range(len(ex1[0]))] for j in range(len(ex1)-1)]
                entropy_sum = [0 for i in range(len(ex1[0]))]
                entropy_sum_value = [0 for i in range(len(ex1[0]))]
                for i in range(0, len(data_array)):
                    data_array[i][0] = (ex1[i+1][0] - ex1[i][0])
                    #data_array[i][1] = (ex1[i+1][1] - ex1[i][1])
                 
                for i in range(0, len(data_array)):
                    entropy_sum[0] = entropy_sum[0] + abs(data_array[i][0])
                    #entropy_sum[1] = entropy_sum[1] + abs(data_array[i][1])

                for i in range(0, len(entropy_array)):
                    if data_array[i][0] == 0:
                        entropy_array[i][0]  = 0.0
                        entropy_array_value[i][0]  = 0.0
                    else:
                        p = 1.0 * abs(data_array[i][0])/entropy_sum[0]
                        #print "p = ", p
                        entropy_array[i][0] = -1.0*math.log(p, 2) * compute_sign(data_array[i][0])
                        entropy_array_value[i][0]  = p * entropy_array[i][0]
                        #entropy_array[i][1] = -1.0*math.log(1.0 * abs(data_array[i][1])/entropy_sum[1], 2) 

                print "entropy_array: ", entropy_array
                print "\n\n\n"
                #print "entropy_array_value: ", entropy_array_value
                return entropy_array, entropy_array_value

def compute_sign_area(data_array):
                inc_area = 0.0
                total_area = 0.0
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

def compute_sign_entropy(data_array):
                inc_area = 0.0
                total_area = 0.0
                for i in range(0, len(data_array)):
                        inc_area = inc_area + data_array[i][0]
                        if data_array[i][0] > 0:
                            total_area = total_area + abs(data_array[i][0])
                        
                inc_memory_ratio = inc_area / total_area
                print 'inc_memory_ratio = ', inc_memory_ratio
                return inc_memory_ratio

def compute_sign_delta(data_array):
                inc_area = 0.0
                total_area = 0.0
                for i in range(0, len(data_array)):
                        inc_area = inc_area + data_array[i][0]
                        if data_array[i][0] > 0:
                            if data_array[i][0] > inc_area:
                                print "the index ",i, "-->", data_array[i][0], ' is possible a peak!'
                            else:
                                total_area = total_area + data_array[i][0]
                        
                inc_memory_ratio = inc_area / total_area
                print 'inc_memory_ratio = ', inc_memory_ratio
                return inc_memory_ratio

def get_sigmoid_value(x):
    return 1.0/(1+math.exp(-x*1.0))

def compute_average_value_area(data_array):
   size = len(data_array)
   ref_value = 0.0
   for i in range(0, size):
           ref_value = ref_value + data_array[i][0]
   ref_value = ref_value / size
   average_area = ref_value * size
   calculator_area = 0.0
   for i in range(1, size):
           calculator_area = calculator_area + compute(data_array[i-1][0], data_array[i][0])
           
   delta_area = calculator_area - average_area
   delta_index = delta_area / ref_value;
   sigmoid_value = get_sigmoid_value(delta_index)
   print 'average area: ', average_area, ', calculator_area: ', calculator_area, ', delta_area: ', delta_area, ", delta_index: ", delta_index
   print 'sigmoid value is ', sigmoid_value
   return sigmoid_value

def compute_simple_value_area(data_array):
   size = len(data_array)
   ref_value = data_array[0][0]
   simple_area = ref_value * size
   calculator_area = 0.0
   for i in range(1, size):
           calculator_area = calculator_area + compute(data_array[i-1][0], data_array[i][0])
           
   delta_area = calculator_area - simple_area
   delta_index = delta_area / simple_area;
   sigmoid_value = 0.0
   sigmoid_delta = 1.0
   if delta_index > 0:
        sigmoid_value = get_sigmoid_value(delta_index)
        print 'sigmoid_value 1 = ', sigmoid_value
        if sigmoid_value < 0.6:
            sigmoid_delta = (sigmoid_value - 0.5) * 10
        sigmoid_value = sigmoid_value * sigmoid_delta
   #else:
   #     sigmoid_value = get_sigmoid_value(delta_index) - 0.5
   print 'ref_value: ', ref_value, ', simple area: ', simple_area, ', calculator_area: ', calculator_area, ', delta_area: ', delta_area, ", delta_index: ", delta_index
   print 'sigmoid value is ', sigmoid_value
   return sigmoid_value

def compute_array(ex1):
                #now we compute memory area for increase or decrease
                data_array, data_array_value = compute_entropy(ex1)
                inc_memory_ratio = compute_sign_entropy(data_array)

                #data_array2 = compute_delta(ex1)
                #inc_memory_ratio2 = compute_sign_delta(data_array2)
                inc_memory_ratio2 = compute_simple_value_area(ex1)
                
                #compute_average_value_area(ex1)

                #inc_memory_ratio2 = compute_sign_entropy(data_array_value)
                #print "data_array2 = ", data_array2

                #sum_value_abs = 0.0
                #sum_value = 0.0
                ##data_array_value = data_array
                #for i in range(0, len(data_array)):
                #    sum_value_abs = sum_value_abs + abs(data_array[i][0])
                #    sum_value = sum_value + data_array[i][0]
                #    #print "i = ",i, ", data =", data_array[i][0] , " sum = ", sum_value
                #
                #print "sum_value = ", sum_value
                #print "sum_value_abs = ", sum_value_abs
                #inc_memory_ratio1 = sum_value/sum_value_abs
                return round(inc_memory_ratio,2), round(inc_memory_ratio2,2)

# test
area1 = compute(3, 4)
print 'area1 = ', area1
area2 = compute(3, -3)
print 'area2 = ', area2
area3 = compute(3, 3)
print 'area3 = ', area3

a1=[[1,0], [2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[100,0],[9,0]]
result1, result2 = compute_array(a1)
print result2
