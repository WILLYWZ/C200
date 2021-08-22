import numpy as np

def tp(a):
    res = np.zeros((len(a[0]),len(a)))
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[j][i]= a[i][j]
    return res

a = np.zeros((4,4),dtype = float)
a[0] = [0,1,1,1]
a[1] = [0,0,0,1]
a[2] = [1,0,0,0]
a[3] = [1,1,0,0]


for i in range(len(a)):
    total = sum(a[i])
    if total ==0:
        continue
    for j in range(len(a[0])):
        a[i][j]= a[i][j]/total

v = np.zeros((4,1),dtype=float)
v[0]=[0.25]
v[1]=[0.25]
v[2]=[0.25]
v[3]=[0.25]

A= a

a = tp(A)

def pr(A,k):
    temp = A
    for n in range(k-2):
        print(n)
        A = np.dot(A,temp)
    return tp(np.dot(A, v))[0]

print(pr(A,8))
