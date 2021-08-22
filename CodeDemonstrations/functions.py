# we want to write a function that adds two numbers
# signature function
# def <function name>(<---->, <---->, ...)
def addition(a,b):
    sum = a+b
    return sum
    print("End of function")

print("C200")
x=12
y=13

s = addition(x,y)
print(s)

# we want to return the max value of 2 variables
def max(x,y):
    if x > y:
        return x 
    else:
        return y
print("Max:", max(5,2))
print("max:", max (23, 23))
print("max:", max(5,2), 9)