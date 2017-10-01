import os
import parse


def get_training_data(pid_name, data_dir):

    exa_index = -1
    files = os.listdir(data_dir)
    files.sort()
    example = [[0 for i in range(2)] for j in range(len(files))]
    print files
    for file_name in files:
            if file_name.find('meminfo') > 0:
                    meminfo = parse.parseLogFile(data_dir + '/' + file_name)
                    if(meminfo.has_key(pid_name)):
                        values0 = meminfo.get(pid_name)
                        if (values0):
                                objects = values0.get('Objects')
                                heaps0 = values0.get('Dalvik Heap ')
                                heaps1 = values0.get('Native Heap ')

                                objects_value = sum(objects)
                                heap_value = heaps0[3] + heaps1[3]
                                #print 'hello ' + str(heaps0[3]) + ' ' + str(heaps1[3])
                                exa_index = exa_index + 1
                                example[exa_index][0] = heap_value
                                example[exa_index][1] = objects_value
                        else:
                                exa_index = exa_index + 1
                                example[exa_index][0] = 0
                                example[exa_index][1] = 0
                    else:
                        print 'no key ......!'
                        exa_index = exa_index + 1
                        example[exa_index][0] = 0
                        example[exa_index][1] = 0

    return example, files



#get_training_data('com.pyzed.androidmemoryleaktest')
#print example
