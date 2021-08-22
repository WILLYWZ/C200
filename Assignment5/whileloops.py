def maxFor(x):
    i=0
    e= x[0]
    while i< len(x):
        if e<i:
            e=i
        i+=1
    return x[e]

def minFor(x):
    i=0
    e= x[0]
    while i< len(xlst):
        if e> xlist[i]:
            e=xlist[i]
        i+=1
    return e

def myremove(x, lst):
    i=0
    l=[]
    while i< len(lst):
        if lst[i] != x:
            l = l +[lst[i]]
        i+=1
    return l

def myReplace(oldX, newX, lst):
    i=0
    l=[]
    while i< len(lst):
        if lst[i] == oldX:
            l = l + [newX]
        else:
            l = l +[lst[i]]
        i+=1
    return l

def myLeftMerge(x, y):
    i=0
    l=[]
    while i< len(x):
        if lst[i] != x:
            l = l +[x[i]]+[y[i]]
        i+=1
    return l

def listProducts(x):
    i=0
    l=[]
    while i< len(x):
       for j in x[i]:
           prod= prod *j
           1+= [prod]
           i+=1
    return l
def removeString(x):
    i=0
    l=[]
    while i< len(x):
        if type(x[i]) != str:
            l = l +[x[i]]
        i+=1
    return l
def removeVowels(x):
    i=0
    l=""
    v= ["a","e","i","o","u","a","A","E","I","O","U"]
    while i< len(x):
        if x[i] not in v:
            l = l +x[i]
        i+=1
    return l

x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [x,y,z]
c = [0,1,1,0,2,1,4]
a = ["a","b","b", "a", "c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]
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