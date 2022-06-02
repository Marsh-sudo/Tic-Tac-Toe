#Two player tic-tac-toe game in python

# 1.Making of dictionary for the board in which keys will be the location .


theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)


# making of a printboard function that prints out the board once a move has been made.

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#making the main function for the game

def main():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Its your turn" + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == '':
            theBoard[move] = turn
            count +=1

        else:
            print("That position is already filled.Move to which place?")
            continue

        #checking if player x or 0 has won after 5 moves.
        if count >= 5 :
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != '': #across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn+ "won. ****")
                break

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '': # across the middle
                printBoard(theBoard)
                print("Game Over")
                print("****" +turn +"won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break  

        #functonality of when the game is tied and board is full
        if count == 9:
            print('\nGame Over.\n')
            print("Its a Tie!!")

        #logic to switch players after every move
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

        #logic to restart the game
        restart = input("Do you wish to play again?(y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theBoard[key] == " "

            main()


if __name__ == "__main__":
    main()