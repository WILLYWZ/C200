import math

def y(d,r,t):
    Dollars = d*math.exp(r*t)
    return Dollars

def N(n_0, m, t):
    Growth = n_0*math.exp(m*t)
    return Growth

def N_t(t):
    Teeth = 71.8*math.exp(-8.96*math.exp(-0.0685*t))
    return Teeth

def D(t):
    Percent = (9/2.6*t)/(2*t**2+3)
    return Percent

def r(t):
    Rent = 1.5207*t**4-19.166*t**3+62.91*t**2+6.0726*t+1026
    return Rent

def p(x):
    Profit = 4*x**2-100*x-1000
    return Profit

def W(p1,p2):
    R = 8.314
    T = 300
    Work = R*T*(math.log(p1/p2))
    return Work

def depreciate(c,s,life):
    Depreciate = (c-s)/life
    return Depreciate

def L(k,V,A,C):
    Lift = k*V**2*A*C
    return Lift

print(y(1000,.02,10))
print(N(500,100,4))
print(math.floor(N_t(1000)))
print(D(1))
print(r(4))
print(p(10))
print(W(10,1))
print(depreciate(20000,1000,5))
print(L(0.0033,33.8,512,0.515))

# 33 is the fewest number of items that makea profit