def roman(n):
    n1={0:"",1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
    n2={0:"",1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
    str= n2[n//10]+n1[n%10]
    return str
    
for i in range(1,100):
        if i % 5 == 0:
            print()
print(i, roman(i), ", ", end="")
