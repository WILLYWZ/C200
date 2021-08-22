def maxFor(x):
    e= x[0]
    i=0
    while i< len(x):
        if e<i:
            e=i
        i+=1
    return x[e]

def remove(xlst, v):
    i=0
    l=[]
    while i< len(xlst):
        if xlst[i] != v:
            l = l +[xlst[i]]
        i+=1
    return l

def min(xlst):
    i=0
    e= xlst[i]
    while i< len(xlst):
        if e> xlst[i]:
            e=xlst[i]
        i+=1
    return e

def second_smallest(xlist):
    a= min(xlist)
    new_list = remove(xlist, a)
    b= min(new_list)
    return b

x = [[1,2,3,4],[4,5,0,1],[22,21,31,10]]

for i in x:
    print(second_smallest(i))

"""
delete lists containing v
def remove(xlst, v):
    result = []
    for i in xlst:
        if v not in i:
            result.append(i)
    return result
"""