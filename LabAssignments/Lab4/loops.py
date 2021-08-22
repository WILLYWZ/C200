def evencount(lst):
    if type(lst)==list:
        count=0
        for i in lst:
            if i%2==0:
                count +=1
        return count
    else:
        return -1


def positionalSumList(list1, list2):
    if type(list1) != list and type(list2)==list:
        return -1
    elif type(list2) != list and type(list1)==list:
        return -2
    elif type(list1) and type(list2) != list:
        return -3
    return positionalSumList(list1, list2)

def lenDictionary(words):
    for "a" in words:
        return 


range(5, 100, 5)

range(20, 60, 2)