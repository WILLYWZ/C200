import random as rn
import numpy as np


def max_index(y):
    max = -999
    f = 0
    g = 0
    for i in range(0,len(y)):
        for j in range(0,len(y)):
            if y[i][j]>max:
                max= y[i][j]
                f=i
                g=j
    data = list()
    data.append(f)
    data.append(g)          

x = rn.randint(3,6)
print(x)
y = np.arange(x**2).reshape(x,x)

for i in range(0,x):
    for j in range(0,x):
        y[i][j] = rn.randint(1,100)

print(y)
i = max_index(y)
print(i)
print(y[i[0]][i[1]])
