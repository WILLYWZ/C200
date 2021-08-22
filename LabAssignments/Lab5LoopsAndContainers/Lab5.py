fruits = ['apple', 'banana', 'orange']
for i in range(len(fruits)):
    print("i:",1)
    print(fruits[i])

i=0
while i<len(fruits):
    print("i:",1)
    print(fruits[i])
    i +=1 

"""
import <python file>
import <python file> as <short name>
from <python file> import <functions>
"""


import numpy as np
ls = [1, 2, 3]
print(type(ls),ls)

ls1=[]
arr = np.array(ls)
arr1 = np.array([8, 9]) 

print(type(arr), arr)
print(type(arr1), arr1)

ls.append(4)
print(ls)
arr = np.append(arr, 4)
print(arr)

ls[1] = "string"
print(ls)

print(arr.dtype)
arr[1] = "string"
print(err)