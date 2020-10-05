theBoard = {
    "TL":" ","TM":" ","TR":" ",
    "ML":" ","MM":" ","MR":" ",
    "BL":" ","BM":" ","BR":" ",
}

def printBoard(board):
    print(board['TL'],'|',board['TM'],'|',board['TR'],sep="")
    print("-+-+-")
    print(board['ML'],'|',board['MM'],'|',board['MR'],sep="")
    print("-+-+-")
    print(board['BL'],'|',board['BM'],'|',board['BR'],sep="")
    print("-+-+-")
def clearBoard(board):
    board['TL'] = " "
    board['TM'] = " "
    board['TR'] = " "
    board['ML'] = " "
    board['MM'] = " "
    board['MR'] = " "
    board['BL'] = " "
    board['BM'] = " "
    board['BR'] = " "
def checkwinner(board):
    if (board['TL'] =='X' and board['TM'] =='X' and board['TR'] == 'X'):
        w = "X"
        return w
    elif(board['TL'] =='O' and board['TM'] =='O' and board['TR'] == 'O'):
        w = "O"
        return w
    elif (board['ML'] =='X' and board['MM'] =='X' and board['MR'] == 'X'):
        w = "X"
        return w
    elif(board['ML'] =='O' and board['MM'] =='O' and board['MR'] == 'O'):
        w = "O"
        return w
    elif (board['BL'] =='X' and board['BM'] =='X' and board['BR'] == 'X'):
        w = "X"
        return w
    elif(board['BL'] =='O' and board['BM'] =='O' and board['BR'] == 'O'):
        w = "O"
        return w
    elif (board['TL'] =='X' and board['MM'] =='X' and board['BR'] == 'X'):
        w = "X"
        return w
    elif(board['TL'] =='O' and board['MM'] =='O' and board['BR'] == 'O'):
        w = "O"
        return w
    elif (board['TR'] =='X' and board['MM'] =='X' and board['BL'] == 'X'):
        w = "X"
        return w
    elif(board['TR'] =='O' and board['MM'] =='O' and board['BL'] == 'O'):
        w = "O"
        return w
    else:
        w = "IC"
        return w

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for',turn,'- enter the position')
    x=input()
    theBoard[x] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    win = checkwinner(theBoard)
    if win == "X":
        print("Player X wins!")
        printBoard(theBoard)
        break
    elif win =="O":
        print("Player O wins!")
        printBoard(theBoard)
        break
    else:
        continue
draw = checkwinner(theBoard)
if draw == "IC":
    print("Draw!")
    printBoard(theBoard)