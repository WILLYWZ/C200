def is_member1(x,ylist):
    if x in ylist:
        return True
    else:
        return False


def is_member2(x,ylist):
    for i in ylist:
        if x == i:
            return True
    return False

def is_member3(x,ylist):
    while x in ylist:
        return True
    return False

def is_member4(x,ylist):
    return x in ylist
       

y = [1,3,5]
x = [1,2,3,4]
for i in y:
    print("1 ", is_member1(i,x))
    print("2 ", is_member2(i,x))
    print("3 ", is_member3(i,x))
    print("4 ", is_member4(i,x))
