#
def circuit(A, B, C):
    def Z(A, B, C):
        X= A and B
        return bool(X or C)
    return bool(not Z(A, B, C) or not C)


print(0,0,0,circuit(0,0,0))
print(0,0,1,circuit(0,0,1))
print(0,1,0,circuit(0,1,0))
print(0,1,1,circuit(0,1,1))
print(1,0,0,circuit(1,0,0))
print(1,0,1,circuit(1,0,1))
print(1,1,0,circuit(1,1,0))
print(1,1,1,circuit(1,1,1))