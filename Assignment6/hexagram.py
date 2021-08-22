
def hex_dec(hex):
    hex = hex[::-1]
    answer = 0
    power = 0
    dict= {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

    for i in hex:
        if i in dict:
            answer = dict[i]*(16**power)
        else:
            answer = int(i)*(16**power)
        power += 1
    return answer


hex = input("Hex: ")
print(hex_dec(hex))