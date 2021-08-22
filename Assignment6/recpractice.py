def s(n):
    if x==0:
        return 0
    else:
        return s(n-1)+n

def s1(n):
    x = n(n+1)/2
    return x

def p(n):
    if n==0:
        return 10000
    else:
        return p(n-1)+0.02*p(n-1)

def p1(n):
    x = (1.02**n)*10000
    return x

def b(n):
    if n==1:
        return 2
    if n==2:
        return 3
    else:
        return b(n-1)+b(n-2)

def c(n):
    if n==1:
        return 9
    else:
        return 9*c(n-1)+10**(n-1)-c(n-1)

def d(n):
    if n==0:
        return 1
    else:
        return 3*d(n-1)+1

def d1(n):
    x = (3**(n+1)-1)/2
    return x