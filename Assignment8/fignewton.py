func_str = input("Fuction: ")
f = lambda x: eval(func_str)
tau = float(input("tau: "))
x0 = float(input("x0: "))
iterations = int(input("Iterations: "))
fp = lambda x: 6*(x**5) - 1

def fpa(f):
    h = .000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)

def newton(f,fp,x,tau):
    def n(x,i):
        while f(x) > tau:
            print("{0} {1:.5f} {2:.5f}".format(i,x,f(x)))
            x = x - f(x)/fp(x)
            i += 1
            if i>= iterations:
                print("number of iterations exceeded ...")
                break
        return x
    n(x,0)

# newton(f,fp,1.5,.0001)
# newton(f,fpa(f),1.5,.0001)
newton(f, fp, x0, tau)
