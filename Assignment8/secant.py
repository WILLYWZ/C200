f = lambda x:x**6-x-1

def secant(f,x0,x1,tau):
    a = x0
    b = x1
    n = 1
    while abs(f(b)) > tau:
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0,f(x0),f(x1),x0-x1))
        b_new = b-f(b)*((b-a)/(f(b)-f(a)))
        a = b
        b = b_new
        n+=1


secant(f,2.0,1.0,.0001)
print()
