import os

#where to store meminfo
mem_info={}
mem_index = -1

def parseHeapDomain(f, pid_name, line, domain_name):
    p = line.find(domain_name)
    if p > -1:
        line = line[p+len(domain_name):len(line)]
        line=line.strip()
        data = line.split()
        mem_info[pid_name][domain_name] = [int(item) for item in data]
        return 1
    else:
        return -1

def parseObjectsDomain(f, pid_name, line, domain_name):
    p = line.find(domain_name)
    if p > -1:
        data=[]
        index = -1
        while True:
            line0 = f.readline().strip()
            if line0:
                temp = line0.split()
                if len(temp) == 6:
                   data.append(int(temp[2]))
                   data.append(int(temp[5]))
                   index = index + 2
                elif len(temp) == 4:
                   data.append(int(temp[1]))
                   data.append(int(temp[3]))
                   index = index + 2
                elif len(temp) == 2:
                   data.append(int(temp[1]))
                   index = index + 1
            else:
                break
        mem_info[pid_name][domain_name] = data
        return 1
    else:
        return -1
    
def parseLogFile(file_name):
        print 'parseLogFile: ' + file_name
        pid_name = ''
        mem_index = -1
        mem_info.clear()
        f = open(file_name,"r")
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                p=line.find('[')
                q=line.rfind(']')
                if p > -1 and q > -1:
                    pid_name=line[p+1:q]
                    if len(pid_name) > 1:
                        mem_index = mem_index + 1
                        mem_info[pid_name] = {}
                else:
                    if parseHeapDomain(f, pid_name, line, 'Native Heap ') > 0:
                        print 'OK\n'
                    elif parseHeapDomain(f, pid_name, line, 'Dalvik Heap ') > 0: 
                        print 'OK\n'
                    elif parseObjectsDomain(f, pid_name, line, 'Objects') > 0:
                        print 'OK\n'
            else:
                break

        f.close()
        return mem_info
