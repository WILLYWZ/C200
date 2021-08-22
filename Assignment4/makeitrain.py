def dollars(x):
    p = int(x * 100)
    q = p // 25
    p -= q * 25
    d = p // 10
    p -= d * 10
    n = p // 5
    p -= n * 5
    
    return [float(num) for num in [q, d, n, p]]

print(dollars(2.24))
print(dollars(1.19)) 
print(dollars(4.16)) 


"""
i use the above to match the answer provided. 
but during my first try,

def dollars(x):
    q=x//0.25
    d=(x-q*0.25)//0.1
    n=((x-q*0.25)-(d*0.1))//0.05
    p=((x-q*0.25)-(d*0.1)-(n*0.05))//0.01
    return [q, d, n, p]

somehow it's off compare to the answer and I couldn't figure out why.
and I got 
[8.0, 2.0, 0.0, 4.0]
[4.0, 1.0, 1.0, 3.0]
[16.0, 1.0, 1.0, 1.0]
 
could you explain it briefly in comments? Thanks.

"""