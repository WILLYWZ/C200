import math

#
def maxThree(x, y, z):
    if x > y and x > z :
        return x
    elif y > x and y > z:
        return y
    else: 
        return z
print(maxThree(1,2,3))

#
def minThree(p1, p2, p3):
    if p1 < p2 and p1 < p3:
        return p1
    elif p2 < p1 and p2 < p3:
        return p2
    else: 
        return p3
print(minThree(10,20,30))

#
def maxTwoSum(tomato, potato, idaho):
    if tomato < potato and tomato < idaho:
        return (potato + idaho)
    elif potato < tomato and potato < idaho:
        return (tomato + idaho)
    else: 
        return idaho
print(maxTwoSum(10,20,30))

#
def minTwoSum(x, y, z):
    if x < y and y < z:
        return x + y
    elif  z < x and x < y:
        return z + x
    else: 
        return y + z
print(minTwoSum(10, 20, 30))

#
def windchill(Ta, V):
    Twc = 34.74 + 0.6215 * Ta- 35.75 * V**0.16 + 0.4275 * Ta * V**0.16
    return Twc
print(windchill(5, 20))

#
def creditcard(APR, C, p):
    i= APR/12*0.01
    n=(-math.log(1-(i*C/p)))/(math.log(i+1))
    return round(n)
print(creditcard(19, 1000, 25))

#
Ta = float(input("Enter Farenhait Temperature: "))
V = float(input("Enter wind speed mph: "))
def windchill(Ta, V):
    Twc = 34.74 + 0.6215 * Ta- 35.75 * V**0.16 + 0.4275 * Ta * V**0.16
    return Twc
print(windchill())

#
APR = float(input("What is your APR: %"))
C = float(input("What is the amount owed on the credit card: $"))
p = float(input("What it the monthly payment made: $"))
def creditcard(APR, C, p):
    i= APR/12*0.01
    n=(-math.log(1-(i*C/p)))/(math.log(i+1))
    return round(n)
print(creditcard())