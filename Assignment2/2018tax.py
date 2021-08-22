# unmarried
def unmarriedTax(income):
    def rate(income):
        if(income >= 0 and income < 9525):
            return 0.1
        elif(income >= 9525 and income < 38700):
            return 0.12
        elif(income >= 38700 and income < 157500):
            return 0.22
        elif(income >= 157500 and income < 200000):
            return 0.24
        elif(income >= 200000 and income < 500000):
            return 0.35
        elif(income >= 500000 ):
            return 0.37
    unmarriedTax = income* rate(income)
    return unmarriedTax

# married
def marriedTax(income):
    def rate(income):
        if(income >= 0 and income < 19050):
            return 0.1
        elif(income >= 19050 and income < 77400):
            return 0.12
        elif(income >= 77400 and income < 315000):
            return 0.22
        elif(income >= 315000 and income < 400000):
            return 0.24
        elif(income >= 400000 and income < 600000):
            return 0.35
        elif(income >= 600000):
            return 0.37
    marriedTax = income* rate(income)
    return marriedTax

#Tax Owe
def tax(income, maritalStatus):
    if(maritalStatus):
        return marriedTax(income)
    else:
        return unmarriedTax(income)

Ursala_married = True
Ursala_income = 252225

Kaiser_married = False
Kaiser_income= 375000

Shilah_married = True
Shilah_income = 77399

print("Ursala owes ", tax(Ursala_income, Ursala_married))
print("Kaiser owes ", tax(Kaiser_income, Kaiser_married))
print("Shilah owes ", tax(Shilah_income, Shilah_married)) 

#marriedtax rate is almost unmarried tax rate, only different in amount of income and the 35%, 37% rate.