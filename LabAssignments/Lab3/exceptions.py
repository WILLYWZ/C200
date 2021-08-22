
# Using the line numbers and errors reported by Python, let's fix our code!


# Total Errors: 1 Syntax Erro
def myAddition(x, y):
    return x + y

#Total Errors: 3 Syntax Errors
def seniorDiscount(age):
    if (age > 65):
        return True
    else:
        return False

# Total Errors: 1 Runtime Error
def inchesInMiles(miles):
    inches = miles * 12 * 5280
    return "There are " + str(inches) + " in " + str(miles) + " miles."

# Total Errors: 1 Runtime Error
def costPerFoot(materialLength, totalCost):
    footCost = totalCost / materialLength
    return str(footCost)



# Total Errors: 2 Syntax, 3 Logical Errors (multiple solutions)
def competitionBracket(age, adultFlag):
    if (age <= 30):
        print("Not Adult Bracket")
    if (age > 30 and age <= 35 and not adultFlag):
        print("Master 1 Bracket")
    if (age > 35 and age <= 40 and not adultFlag):
        print("Master 2 Bracket")
    if (age > 40 and age <= 45 and not adultFlag):
        print("Master 3 Bracket")
    if (age > 30 and adultflag):
        print("Adult Bracket")




# Our function calls for testing

print(myAddition(5, 5), " = ", 10)
print("Do you get a senior discount? ", seniorDiscount(66))
print("Do you get a senior discount? ", seniorDiscount(26))
print(inchesInMiles(2.5))
print(costPerFoot(20, 1000))
print(costPerFoot(0, 100))

## should be adult bracket
competitionBracket(22, True)
print()
## should be master 3 bracket
competitionBracket(43, False)
print()
## should be adult bracket
competitionBracket(36, True)