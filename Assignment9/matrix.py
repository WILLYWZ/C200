import numpy as np
#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    value = np.zeros((len(a),len(b[0])))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                value[i][j] += a[i][k]*b[k][j]
    return value

#INPUT scalar n and matrix a
#RETURN scalar product na
def sm(n,a):
    value = np.zeros((len(a),len(a[0])))
    for i in range(len(a)):
        for j in range(len(a[0])):
            value[i][j] = 4*a[i][j]
    return value

#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    value = np.zeros((len(a[0]), len(a)))
    for i in range(len(a)):
        for j in range(len(a[0])):
            value[j][i] = a[i][j]
    return value

#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    value = np.zeros((len(a),len(b[0])))
    for i in range(len(a)):
        for j in range(len(b[0])):
            value[i][j] = a[i][j] + b[i][j]
    return value

a = np.array([[1,2,4],[3,4,3]])
b = np.array([[-1,0],[1,-5],[-3,1]])
print("numpy product\n", np.dot(a,b))
d = mm(a,b)
print(d)

print("numpy scalar product\n", 4*a)
e = sm(4,a)
print(e)

print("numpy tranpose\n", np.transpose(a))
f = tp(a)
print(f)

print("numpy addition\n", a + a)
g = add_m(a,a)
print(g)
