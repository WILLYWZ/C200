def F(A,B,Cin):
    F=(A^B)^Cin
    return F

#inputs signals A,B, Cin
def G(A,B, Cin):
    G=(A and B)or((A^B) and Cin)
    return G
signals = [0,1]
for A in signals:
    for B in signals:
        for Cin in signals:
                print(A,B,Cin,F(A,B,Cin),G(A,B,Cin))
