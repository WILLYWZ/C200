import numpy as np
import random as rn

class TTT:
    def __init__(self):
        self.b = np.array([1,2,3,4,5,6,7,8,9])
        self.moves = [1,2,3,4,5,6,7,8,9]
        self.game = []

    def pt(self, x):
        if (x == 0):
            return "x"
        elif (x == -1):
            return "o"
        else:
            return str(x)

    def win(self, player):
        if player[0] == 0 and player[1] == 0 and player[2] == 0:
            print("x wins!")
            return 1 
        elif player[3] == 0 and player[4] == 0 and player[5] == 0:
            print("x wins!")
            return 1 
        elif player[6] == 0 and player[7] == 0 and player[8] == 0:
            print("x wins!")
            return 1 
        elif player[0] == 0 and player[3] == 0 and player[6] == 0:
            print("x wins!")
            return 1 
        elif player[1] == 0 and player[4] == 0 and player[7] == 0:
            print("x wins!")
            return 1 
        elif player[2] == 0 and player[5] == 0 and player[8] == 0:
            print("x wins!")
            return 1 
        elif player[2] == 0 and player[4] == 0 and player[6] == 0:
            print("x wins!")
            return 1 
        elif player[0] == 0 and player[4] == 0 and player[8] == 0:
            print("x wins!")
            return 1 

        if player[0] == -1 and player[1] == -1 and player[2] == -1:
            print("o wins!")
            return 1 
        elif player[3] == -1 and player[4] == -1 and player[5] == -1:
            print("o wins!")
            return 1 
        elif player[6] == -1 and player[7] == -1 and player[8] == -1:
            print("o wins!")
            return 1 
        elif player[0] == -1 and player[3] == -1 and player[6] == -1:
            print("o wins!")
            return 1 
        elif player[1] == -1 and player[4] == -1 and player[7] == -1:
            print("o wins!")
            return 1 
        elif player[2] == -1 and player[5] == -1 and player[8] == -1:
            print("o wins!")
            return 1 
        elif player[2] == -1 and player[4] == -1 and player[6] == -1:
            print("o wins!")
            return 1 
        elif player[0] == -1 and player[4] == -1 and player[8] == -1:
            print("o wins!")
            return 1
        return 0
       
          
    def board(self):
        print()
        for i in range(0,3):
            print("{0:^3}|{1:^3}|{2:^3}".format(self.pt(self.b[i+i*2]),self.pt(self.b[i+1+i*2]),self.pt(self.b[i+2+i*2])))
            if i < 2:
                print("=== === ===")

    def play(self, x = "x"):
        self.board()
        if x == "x":
            while True:
                print(self.moves)
                key = int(input("[1, 2, 4, 5, 6, 7, 8, 9] 5" ))
                self.b[key - 1] = 0
                self.moves.remove(key)
                flag = self.win(self.b)
                if len(self.moves) == 0:
                    print("tie")
                elif flag == 1:
                    self.b[key - 1] = -1
                    self.moves.remove(key)
                    flag = self.win(self.b)
                    self.board()
        else: 
             while True:
                key = rn.choice(self.moves)
                self.b[key - 1] = 0
                self.moves.remove(key)
                flag = self.win(self.b)
                self.board()

                if len(self.moves) == 0:
                    print("tie")
                    break
                if flag == 1:
                    self.b[key - 1] = -1
                    self.moves.remove(key)
                    flag = self.win(self.b)
                    self.board()

x = TTT() 
x.play('o')

'''
i understand the concept but i have no idea how to fix it
could you provide a code of answer for this?
'''