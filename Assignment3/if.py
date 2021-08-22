x = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True

#1 Rewrite this as an eqiuvalent if-elif-else
if b:
    print("Happy")
elif not b and x:
    print("Valentines")
else:
    print("day!")

#2 Rewrite as an equivalent two if statements
if (z > a):
    print("C200")
if (2*a > z):
    print("C200")

#3 Rewrite the conditional using as few not’s as possible
if not ((a and b and z) or (y and z and a and b)):
    print(a)

#4 Rewrite this as four single if statements.
if (2 > z) or x:
    print("1")
if 2 == 1:
    print("2")
if y and not x:
    print("3")
if not(((2 > z) or x) and (2 == 1) and (y and not x)):
    print("4")

#5 Rewrite this as an if-elif-else. The output of the prints are shown below.
def f(x):
    if x == 4:
        return (x==4)*100
    elif x == 3:
        return (x==3)*10
    elif x == 2:
        return (x==2)*1000
    else:
        return (x!=4)*(x!=3)*(x!=2)*100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))


"""
I'm confused with the question prompt.
#1 Rewrite this as an eqiuvalent if-elif-else.
#2 Rewrite as an equivalent two if statements.
#2 Rewrite the conditional using as few not’s as possible.
#3 Rewrite this as four single if statements.
#4 Rewrite this as an if-elif-else.

two #2? should not it be #3 for the second #2, #4 be #3 and #5 be #4?
#1, #2, #3, #4, #5 is what I do.
"""
