def printboard(xState, zState):
    print(f"{xState[0] if xState[0] else ('O' if zState[0] else 1)} | {xState[1] if xState[1] else ('O' if zState[1] else 2)} | {xState[2] if xState[2] else ('O' if zState[2] else 3)}")
    print("--|---|---")
    print(f"{xState[3] if xState[3] else ('O' if zState[3] else 4)} | {xState[4] if xState[4] else ('O' if zState[4] else 5)} | {xState[5] if xState[5] else ('O' if zState[5] else 6)}")
    print("--|---|---")
    print(f"{xState[6] if xState[6] else ('O' if zState[6] else 7)} | {xState[7] if xState[7] else ('O' if zState[7] else 8)} | {xState[8] if xState[8] else ('O' if zState[8] else 9)}")

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to tic tac toe")
    while True:
        printboard(xState, zState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value - 1] = 'X'
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value - 1] = 'O'
        if turn == 1:
            turn = 0
        else:
            turn = 1
        # check for winning condition
        for i in range(0, 9, 3):
            if xState[i:i+3] == ['X', 'X', 'X']:
                print("X has won!")
                exit()
            elif zState[i:i+3] == ['O', 'O', 'O']:
                print("O has won!")
                exit()
        for i in range(3):
            if xState[i::3] == ['X', 'X', 'X']:
                print("X has won!")
                exit()
            elif zState[i::3] == ['O', 'O', 'O']:
                print("O has won!")
                exit()
        if xState[0] == xState[4] == xState[8] == 'X' or xState[2] == xState[4] == xState[6] == 'X':
            print("X has won")
