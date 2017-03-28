import os

#where to store meminfo
mem_info={}
mem_index = -1
pid_name = None

def parseDomain(pid_name, line, domain_name):
    p = line.find(domain_name)
    if p > -1:
        line = line[p+len(domain_name):len(line)]
        line=line.strip()
        data = line.split()
        mem_info[pid_name][domain_name] = data
        print data
        return 1
    else:
        return -1

f = open("tencent.meminfo","r")
while True:
    line = f.readline()
    if line:
        line = line.strip()
        p=line.find('[')
        q=line.rfind(']')
        if p > -1 and q > -1:
            pid_name=line[p+1:q]
            if pid_name:
                mem_index = mem_index + 1
                mem_info[pid_name] = {}
                print pid_name
        else:
            if parseDomain(pid_name, line, 'Native Heap ') > 0:
                print 'OK\n'
            elif parseDomain(pid_name, line, 'Dalvik Heap ') > 0: 
                print 'OK\n'
    else:
        break

f.close()

print mem_info
print mem_index
