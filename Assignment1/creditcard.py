# get library for log function
import math

# get user inputs
APR = float(input("What is your APR: %"))
C = float(input("What is the amount owed on the credit card: $"))
p = float(input("What it the monthly payment made: $"))

#complete code here

DPR= APR/360
i= APR/12*0.01
n=(-math.log(1-(i*C/p)))/(math.log(i+1))

print("You’ll make ", math.ceil(n), " payments.")