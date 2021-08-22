
a = int(input("Do you have admonial pain: 1/0 "))
n = int(input("Do you have nausea: 1/0 "))
v = int(input("Do you have vomiting: 1/0 "))
# if meet three condition, stop the code, return answer
if a+n+v == 3:
    print("Appendicitis")
else:
    f = int(input("Do you have fever: 1/0 "))
    if a+n+v+f == 3:
        print("Appendicitis")
    else:
        l = int(input("Do you have loss of appetite: 1/0 "))
        if a+n+v+f+l >= 3:
            print("Appendicitis")
        else:
            print("No Appendicitis.")