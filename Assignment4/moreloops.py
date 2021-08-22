x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [x,y,z]
c = [0,1,1,0,2,1,4]
a = ["a","b","b", "a", "c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]

def maxFor(x):
    max=x[0]
    for i in x:
        if max<i:
            max=i
    return max

def minFor(x):
     min=x[0]
     for i in x:
         if min>i:
             min=i
     return min


def myRemove(x, lst):
    list =[]
    for i in lst:
        if i !=x:
            list=list+[i]
    return list

def myReplace(oldX, newX, lst):
    list =[]
    for i in range(len(lst)):
        if lst[i]==oldX:
            list=list+[newX]
        else:
            list=list+[lst[i]]
    return list

def myLeftMerge(x, y):
    list =[]
    for i in range(len(x)):
        if i !=x:
            list=list+[x[i]]+[y[i]]
    return list

def listProducts(x):
    list=[]
    for i in x:
        product=1
        for j in i:
            product=product*j
        list +=[product]
    return list

def removeString(x):
    list=[]
    for i in lst:
        if i != str:
             list=list+[i]
    return list
def removeVowels(x):
    list=[]
    for i in lst:
        if i !=str:
             list=list+[i]
    return list


for i in nlst:
    print(minFor(i))
    print(maxFor(i))

print(myRemove("a",a))
print(myRemove("b",a))
print(myRemove("z",a))
print(myRemove(1,b))
print(myRemove(2,b))
print(myRemove("a",b))
print(myReplace("a",":)",a))
print(myReplace(1,0,b))
print(removeVowels("the lazy brown fox jumped over the eager dog"))
print(listProducts([[1],[2,3,4],[10,10,10,10]]))
print(removeString(["This",1, "is", "very", 3, [4], "exciting"]))
print(myLeftMerge(a,b))
print(myLeftMerge(['aa','bb'],[1,2]))