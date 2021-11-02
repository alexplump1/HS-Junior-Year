from TicTacToeScore import Score
import time
X=Score()
O=Score()

def print_TTT(board):
    l = "  | ";
    for r in range(3):
        print(board[r][0]+l+board[r][1]+l+board[r][2])
        if (r < 2):
            print(12*"-")
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
resetBoard = [[" "," "," "],[" "," "," "],[" "," "," "]];
#print_TTT(board)
XorO = "X";
def TTT(XorO):
    global board;
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    global resetBoard;
    print("")
    print("TicTacToe has been started. ")
    print("Remeber rows go left to right, and coloumns go top to bottom.")
    time.sleep(3);
    #board=resetBoard
    print_TTT(board)
    TTTdone = False;
    TTTPlayed = False;
    list123 = [0,1,2]
    while TTTdone == False:                  #Making sure game isn't over
        TTTPlayed=False;
        for i in list123:                   #Checink 1 person
            if board[i][0]==XorO and board[i][1]==XorO and board[i][2]==XorO:                         #Checking horizontal outcomes.
                TTTDone = True;
                for i in board:
                    i = [" "," "," "]
                print_TTT(board)
                if XorO == "X":
                    X.addScore()
                    print("X score- "+str(X.score))
                    print("X has won")
                elif XorO == "O":
                    O.addScore()
                    print("O score- "+str(O.score))
                    print("O has won")
                TTT(XorO)
            elif board[0][i]==XorO and board[1][i]==XorO and board[2][i]==XorO:                         #Checking vertical outcomes
                TTTDone = True;
                if XorO == "X":
                    X.addScore()
                    print("X score- "+str(X.score))
                    print("X has won")
                elif XorO == "O":
                    O.addScore()
                    print("O score- "+str(O.score))
                    print("O has won")
                    TTT(XorO)
        if board[0][2]==XorO and board[1][1]==XorO and board[2][0]==XorO:                         #Checking diagonal
            TTTDone = True;
            if XorO == "X":
                X.addScore()
                print("X score- "+str(X.score))
                print("X has won")
            elif XorO == "O":
                O.addScore()
                print("O score- "+str(O.score))
                print("O has won")
                TTT(XorO)
        elif board[0][0]==XorO and board[1][1]==XorO and board[2][2]==XorO:                         #Checking other diagonal
            TTTDone = True;
            if XorO == "X":
                X.addScore()
                print("X score- "+str(X.score))
                print("X has won")
            elif XorO == "O":
                O.addScore()
                print("O score- "+str(O.score))
                print("O has won")
                TTT(XorO)
        if XorO == "X":
            XorO = "O"
        elif XorO == "O":
            XorO = "X";
        #print("done checking")
        if TTTdone != True:    
            while TTTPlayed == False:                                               #Making sure player answered
                row = input("Row: ")
                col = input("Column: ")
                if row >= 1 and row <= 3 and col >= 1 and col <= 3:     #checks if coordinate is on grid
                    if board[int(row)-1][int(col)-1] == " ":             #checks if the space is empty
                        board[int(row)-1][int(col)-1] = XorO;           #fills space 
                        TTTPlayed = True;                               #end loop
                        print_TTT(board)                                #reprint board
                    else:
                        print("That space is already taken")
                        TTTPlayed = False;
                else:
                    print("That coordinate is not on the grid")
                    TTTPlayed = False;
        #if TTTdone == True:
        #    print_TTT(board)
    
playTTT = raw_input("Would you like to play Tic Tac Toe? ")
if playTTT.lower() == "yes":
    TTT(XorO);