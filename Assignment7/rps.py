import random as rn
def get_best_move(rules, history):
    move = ""
    if history["r"] >= history["p"] and history["r"] >= history["s"]:
        move = "r"
    elif history["p"] >= history["r"] and history["p"] >= history["s"]:
        move = "p"
    elif history["s"] >= history["r"] and history["s"] >= history["p"]:
        move = "s" 

    for i in rules:
        if i[1] == move:
            return i[0]


def RPS(n):

    rules = [["r","s"],["p","r"],["s","p"]]
    wins = 0
    ties = 0
    losses = 0
    moves = ["r", "s", "p"]
    cnt = 0

    history = {"r":0, "p":0, "s":0}

    while cnt <= n:
        x = input("play: ")
        m = get_best_move(rules, history)
        if x == m:
            ties =+ 1
            print("tie")
        elif [x,m] in rules:
            print("human wins {0} beats {1}".format(x,m))
            wins += 1
        else:
            losses += 1
            print("robot wins {0} beats {1}".format(m,x))
        cnt += 1
        
                
    print("human wins : {0}".format(wins))
    print("robot wins : {0}".format(losses))
    print("ties: {0}".format(ties))

t = int(input("How many games: "))
RPS(t)

