
def replace(new,old,x):
    lst= []
    for i in x:
        if i == old:
            lst.append(new)
        else:
            lst.append(i)
    return lst

def REPLACE(new,old,lst):
    if len(lst) == 1:
        if lst[0] ==old:
            return [new]
        else:
            return lst
    elif lst[0] ==old:
        return [new] + REPLACE(new, old, lst[1:])
    else:
        return [lst[0]] + REPLACE(new, old, lst[1:])




x = [1,3,2,4,2,1,1,2,2,1]
print(REPLACE(10,1,x))
print(REPLACE(1,3,REPLACE(1,3,x)))