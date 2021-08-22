
import math

def simpson(fn,a,b,n):
    delta_x = (b - a)/n
    interval = lambda i: a + i*delta_x
    lst= [interval(i) for i in range(n+1)]
    fx = [fn(i) for i in lst]

    r = 0
    for i in range(n +1):
        if i == 0 or i == n:
            r += fx[i]
        elif i%2 == 0:
            r = 2*fx[i]
        else:
            r = 4*fx[i]
    return (b-a)/(3*n)*r

def convert(x):
    if x.isnumeric():
        return float(x)
    else:
        return eval(x)

with open("integralfile.txt", "r") as xfile:
    xlines = [d.split(",") for d in xfile.read().split("\n")]

for i in xlines:
    body = i[0]
    fn = eval("lambda x : " + body)
    a = convert(i[1])
    b = convert(i[2])
    n = convert(i[3])
    answer = convert(i[4])
    integration = simpson(fn,a,b,n)
    error = abs((answer - integration)/answer)
    print("f(x) = {0} over [{1},{2}] is {3:.3f}".format(body,a,b,integration))
    print("Actual answer is {0:.3f}".format(answer))
    print("Error is {0:.3f}".format(error))