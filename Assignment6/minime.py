def min(x,y):
    if x < y:
        return x
    else:
        return y

def MIN(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], min(lst[1:])

def min1(x):
    min = 0
    for i in range(1, len(x)):
        if x[i] < x[min]:
            min = i
    return x[min]

def min2(x):
    small = x[0]
    for i in x[:-1]:
        if i < small:
            small = i
    return small

def min3(x):
    small = x[0]
    for i in range(1, len(x), 1):
         small = min(small,x[i])
    return small

def min4(x):
    small = x[0]
    while x[i] < small:
        small = min(small, i)
    return small

def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

x = [1,42,-1,22,0,12]
mf = [MIN, min1, min2, min3, min4, min5]

for f in mf:
    print("{0}({1}) = {2}".format(f.__name__,x,f(x)))



"""
i'm not so sure what min1 min2 min3 min4 want me to do, find min?
by the way
min1 min2 min3 min4 works seperately (if question wants min)
but not together 
it said syntax error
"""