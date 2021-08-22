file = open("acme_zyx.txt.","w")

file.write("[62.50, 85.40]\n")
file.write("[112.0, 202.55]\n")
file.write("[62.00, 103.55]\n")
file.write("[122.5, 202.15]\n")
file.write("[55.00, 98.90]\n")
file.write("[75.50,  151.10]\n")
file.write("[117.50, 181.85]\n")
file.write("[118.50, 197.30]\n")
file.write("[59.50, 85.70]\n")
file.write("[121.50, 195.20]")
file.close()

import math
import matplotlib.pyplot as plt
import numpy as np

def mean(lst):
    mean = sum(lst)/ len(lst)
    return mean

def sd(xlst):
    sum = 0
    m = mean(xlst)
    for x in xlst:
        sum = sum + (x-m)**2
        value = sum / (len(xlst)-1)
    return value


file = open("acme_zyx.txt.","r")
x = file.read()
listx=list()
listy=list()


for i in x:
    listx.append(i[0])
    listy.append(i[1])

mean_x = mean(listx)
mean_y = mean(listy)
sd_x = sd(listx)
sd_y = sd(listy)
value = 0

for i in range(len(listx)):
    a = (listx[i]-mean_x) / (sd_x**2)
    b = (listy[i]-mean_y) / (sd_y**2)
    value += a * b

r = value / (len(listx)-1)

print(r)
plt.plot([i[0] for i in x],[i[1] for i in x],'ro')
t = np.arange(0,6,.1)
plt.plot(t,t*.65 + .5,'g--')
plt.axis([0,6,0,6])
plt.xlabel("A values")
plt.ylabel("B value")
plt.title("stock.png".format(r))
plt.show()

'''
i know there is a str index out of range since there could only be 0,1,2,3,4,5,6,7,8 for i
i have no idea how to solve it
'''