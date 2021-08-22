import math
# Data $/ounce
gold = 1341.30
silver = 17.19
platinum = 1005.00
palladium = 1057.95

#1
#Parameters gold oz g_oz, silver oz s_oz, platinum oz pl_oz, palladium oz pa_oz
#Return the $ amount of the holdings

def cost(g_oz, s_oz, pl_oz, pa_oz):
    cost = g_oz*gold+s_oz*silver+pl_oz*platinum+pa_oz*palladium
    return cost

#2
#Parameters $/oz of metal value and $ amount to spend money
#Return the most WHOLE ounces that can be purchased with the money

def how_many_oz(value, money):
    amount = math.floor(money/value)
    return amount

#3
#Parameters number of ounces of a metal metal_oz, and the metal
#Return the amount of $ the amount is worth

def value(metal_oz, metal):
    def name(metal):
        if metal == "Au":
            return gold
        elif metal == "Ag":
            return silver
        elif metal == "Pd":
            return palladium
        elif metal == "Pt":
            return platinum
    worth = name(metal)*metal_oz
    return worth

print(cost(3,0,0,0))
print(cost(0,2,0,0))
print(cost(0,0,3,0))
print(cost(0,0,0,2))
print(cost(3,1,4,5))
print(cost(2,400,3,4))

print(how_many_oz(gold,2.5*gold))
print(how_many_oz(silver,4*silver))
print(how_many_oz(platinum,math.pi*platinum))
print(how_many_oz(palladium,10/2*palladium))

print(value(10, "Au"))
print(value(10, "Ag"))
print(value(10, "Pd"))
print(value(10, "Pt"))