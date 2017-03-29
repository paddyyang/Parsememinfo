import os
import parse

example = [[0 for i in range(2)] for i in range(10)]

def get_training_data(pid_name):

    exa_index = -1
    files = os.listdir('./')
    print files
    for file_name in files:
            if file_name.find('meminfo') > 0:
                    meminfo = parse.parseLogFile(file_name)
                    if(meminfo.has_key(pid_name)):
                        values0 = meminfo.get(pid_name)
                        objects = values0.get('Objects')
                        heaps0 = values0.get('Dalvik Heap ')
                        heaps1 = values0.get('Native Heap ')

                        objects_value = sum(objects)
                        heap_value = heaps0[3] + heaps1[3]
                        exa_index = exa_index + 1
                        example[exa_index][0] = heap_value
                        example[exa_index][1] = objects_value



get_training_data('com.anydo')
print example
