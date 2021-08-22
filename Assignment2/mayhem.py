s1 =75
# miles/hours
t1 = 4
# hours
t2 = 2020
# min
t3 = 414241
# sec
d1 = 100
# miles
d2 = 1442412
# feet

import math

#1
def speed(d,t):
    speed = d/t
    return speed

#2
def distance(s,t):
    distance = s*t
    return distance

#3
def time(s, d):
    time = d/s
    return time

#4
def hours_to_min(numberHours):
    min = numberHours*60
    return min

#5
def min_to_sec(numberMinutes):
    sec = numberMinutes*60
    return sec

#6
def feet_to_mile(numberFeet):
    mile = numberFeet/5280
    return mile

#7
def miles_to_kilometers(numberMiles):
    kilometers = numberMiles*1.60934
    return kilometers

#8
def kilometers_to_miles(numberKilometers):
    Miles = numberKilometers/1.60934
    return Miles

#9
def miles_to_feet(numberMiles):
    feet = numberMiles*5280
    return feet

#10
def degrees_to_radians(numberDegrees):
    radians = numberDegrees*math.pi/180
    return radians

#11
def side_length_triangle(a, b, gamma):
    angle = gamma*math.pi/180
    side_length_triangle= math.sqrt(a**2+b**2-2*a*b*math.cos(angle))
    return side_length_triangle

#12
def celsius_to_fahrenheit(numberDegreesC):
    fahrenheit = numberDegreesC*(9/5)+32
    return fahrenheit

#13
def fahrenheit_to_celsius(numberDegreesF):
    celesius = (numberDegreesF-32)*5/9
    return celesius

#14
def kelvin_to_fahrenheit(numberKelvin):
    fahrenheit = (9/5)*(numberKelvin-273)+32
    return fahrenheit

#15
def percent_change(p, d):
    percent_change = d/p
    return percent_change

#16
def parsecs_to_kilometers(numberParsecs):
    kilometers = numberParsecs*3.086*10**13
    return kilometers

#17
def lightyears_to_parsecs(numberLightYears):
    parsecs = numberLightYears/3.26
    return parsecs

print(speed(d1,t1), "miles/hour")
print(miles_to_kilometers(speed(d1,t1)), "kilometers/hour")
print(miles_to_kilometers(speed(d1,t1))/min_to_sec(hours_to_min(1)), "kilometers/sec")
print(celsius_to_fahrenheit(-30), "Fahrenheit")
print(min_to_sec(hours_to_min(1)), "seconds")
print(fahrenheit_to_celsius(-22), "Celcius")
print(celsius_to_fahrenheit(20), "Fahrenheit")
print(kelvin_to_fahrenheit(293), "Fahrenheit")
print(fahrenheit_to_celsius(kelvin_to_fahrenheit(293)), "Celcius")
print(side_length_triangle(8,11,37), " units")
print(degrees_to_radians(30), "radians")
print(percent_change(170.90,3.31), "percent change")
print(percent_change(170.90,-3.31), "percent change")
print(parsecs_to_kilometers(231), "kilometers")
print(kilometers_to_miles(parsecs_to_kilometers(lightyears_to_parsecs(3.5))), "miles")