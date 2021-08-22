f = lambda x:x**6-x-1

def sign(x):
    if f(x) > 0:
        return 1
    else:
        return -1

def bisect(f,a,b,tau):
    c=(a+b)/2
    n=1
    while (b-c)> tau:
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))

        if sign(f(b))*sign(f(c))<=0:
            a = c
        else:
            b = c
        c=(a+b)/2
        n += 1

bisect(f,1.0,2.0,.001)