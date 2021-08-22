import matplotlib.pyplot as plt
import numpy as np

Data = [(62.50, 85.40),(112.0, 202.55),
       (62.00, 103.55),(122.5, 202.15),
       (55.00, 98.90),(75.50, 151.10),
       (117.50, 181.85), (118.50, 197.30),
       (59.50, 85.70), (121.50, 195.20)]

X = np.zeros((10,2),dtype = int)
Y = np.zeros((10,1),dtype = int)

for r in range(0,len(Data)):
    X[r][1] = Data[r][0]
    Y[r][0] = Data[r][1]
   
def transpose(a):
    value = np.zeros((len(a[0]), len(a)))
    for i in range(len(a)):
        for j in range(len(a[0])):
            value[j][i] = a[i][j]
    return value

    
XtX = np.dot(transpose(X),X)
XtY = np.dot(transpose(X),Y)
Betas = np.dot (np.linalg.inv(XtX),XtY)
print(Betas)

xp = [i[0] for i in Data]
yp = [i[1] for i in Data]
plt.plot(xp,yp,'ro')
t = np.arange(0.,10,1)
plt.plot(t,Betas[0][0]+Betas[1][0]*t,'g--')
plt.axis([0,8,0,4])
plt.show()

"""
i have no idea what this problem is asking.
and no matter what i try with the code, it always give me "singular matrix'
which i dont understand, how come two random matrix times together equal to 0?
"""