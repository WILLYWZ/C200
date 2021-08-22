import numpy as np
import matplotlib.pyplot as plt

g = np.zeros(10)

def error(s, x):
    v = (s-x**2)/(2*x)
    return abs(v)

def bakhshali(s, epsilon, estimate):
    x = estimate
    i = 0
    g[i] = x
    if error(s,estimate) <= epsilon:
        return x
    sq = (s - estimate**2)/(2 * estimate)
    return sq

def square_root(s,epsilon,estimate):
    x = estimate
    i = 0
    g[i] = x
    while error(s,x) > epsilon:
        i += 1
        x = (x + s/x)*(1/2)
        g[i] = x
    return x

t1 = np.arange(1,8,1)

plt.ylabel("Final Estimate")
plt.xlabel("Iterations")
plt.title("Convergence of Square Root")

"""
in order for the code to run,
the float point value could not be g.
so i change g = square_root() -> s = square_root()
and print(g) -> print(s)
"""

s = square_root(1000,.00005,500)
print(s)
plt.plot(t1,g[t1],'r-o')

s = square_root(1000,.00005,775)
print(s)
plt.plot(t1,g[t1],'b-o')

s = square_root(1000,.00005,3)
print(s)
plt.plot(t1,g[t1],'g-o')

plt.show()