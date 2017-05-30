import os

#
#  use 'adb shell dumpsys activity top' command
#  will give us the current activity name
#

def compute(a, b):
    if a * b < 0:
        h1 = abs(a)/(abs(a) + abs(b))
        h2 = abs(b)/(abs(a) + abs(b))
        area = a*h1/2.0 + b*h2/2.0 
        return area
    else:
        area = (a + b) * 1 / 2.0
        return area

def compute_all(a, b):
    if a * b < 0:
        h1 = abs(a)/(abs(a) + abs(b))
        h2 = abs(b)/(abs(a) + abs(b))
        area = abs(a)*h1/2.0 + abs(b)*h2/2.0 
        return area
    else:
        area = (abs(a) + abs(b)) * 1 / 2.0
        return area


# test
area1 = compute(3, 4)
print 'area1 = ', area1
area2 = compute(3, -3)
print 'area2 = ', area2
area3 = compute(3, 3)
print 'area3 = ', area3
