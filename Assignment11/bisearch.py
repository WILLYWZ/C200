import random as rn
import math
import numpy as np
import time

def bs(T,L,R):
    R= R-1
    while L<=R:
        mid = (L+R)//2
        if T < a[mid]:
            R = mid -1
        elif T > a[mid]:
            R = mid +1
        else:
            return mid
    return -1


size = 100000000
a = np.zeros(size,dtype = int)
for i in range(0,size):
    a[i] = int(rn.gauss(100000,40000))

key = a[rn.randint(0,size)]


print("Looking for {0}".format(key))

print("Linear Search...")
print("Starting {0}".format(time.time()))

found = False
for i in range(0,size):
    if a[i] == key:
        found = True
        break
    print("Ending time {0}".format(time.time()))

print("\nQuicksort...")
#default is quicksort
a.sort()
print("BFS...")
print("Starting {0}".format(time.time()))

x = bs(key,0,size)
print("Ending time {0}".format(time.time()))