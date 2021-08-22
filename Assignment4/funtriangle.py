#1
for i in range(1,10,1):
    print(i*"*")
for i in range(10,0,-1):
    print(i*"*")

#2
step=0
for i in range(1,10,1):
    step=step+i
    print(step*"*")
for i in range(9,1,-1):
    step=step-i
    print(step*"*")

#3
step= 23
for i in range(0,11,1):
    step=step-2
    print(i*" "+step*"*")
