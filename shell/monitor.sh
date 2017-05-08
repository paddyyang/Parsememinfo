#!/bin/sh
while [ 1 ]
do
    echo "uptime"  
    uptime  
      
    echo "cat /proc/cpuinfo"  
    cat /proc/cpuinfo  
              
    echo "top -n 1 -d 1 -m 30 -t"  
    top -n 1 -d 1 -m 30 -t  
                     
    echo "procrank"  
    procrank  
                                       
    echo "cat /proc/vmstat"  
    cat /proc/vmstat  
                                                  
    echo "cat /proc/vmallocinfo"  
    cat /proc/vmallocinfo  
                                                           
    echo "cat /proc/slabinfo"  
    cat /proc/slabinfo  
                                                                      
    echo "cat /proc/zoneinfo"  
    cat /proc/zoneinfo  
                                                                               
    busybox sleep 60  
done
