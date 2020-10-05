#1)                                              The Knight’s tour problem

# Python3 program to solve Knight Tour problem using Backtracking
 
# Chessboard Size
n = 8
 
 
def isSafe(x, y, board):
    '''
        A utility function to check if i,j are valid indexes 
        for N*N chessboard
    '''
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False
 
 
def printSolution(n, board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
 
 
def solveKT(n):
    '''
        This function solves the Knight Tour problem using 
        Backtracking. This function mainly uses solveKTUtil() 
        to solve the problem. It returns false if no complete 
        tour is possible, otherwise return true and prints the 
        tour. 
        Please note that there may be more than one solutions, 
        this function prints one of the feasible solutions.
    '''
 
    # Initialization of Board matrix
    board = [[-1 for i in range(n)]for i in range(n)]
 
    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    # Since the Knight is initially at the first block
    board[0][0] = 0
 
    # Step counter for knight's position
    pos = 1
 
    # Checking if solution exists or not
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(n, board)
 
 
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    '''
        A recursive utility function to solve Knight Tour 
        problem
    '''
 
    if(pos == n**2):
        return True
 
    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
 
            # Backtracking
            board[new_x][new_y] = -1
    return False
 
 
# Driver Code
if __name__ == "__main__":
     
    # Function Call
    solveKT(n)


    


#2)                                                   N Queen Problem 

# Python3 program to solve N Queen  
# Problem using backtracking 
global N 
N = 4
  
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 
  
# A utility function to check if a queen can 
# be placed on board[row][col]. Note that this 
# function is called when "col" queens are 
# already placed in columns from 0 to col -1. 
# So we need to check only left side for 
# attacking queens 
def isSafe(board, row, col): 
  
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True
  
def solveNQUtil(board, col): 
      
    # base case: If all queens are placed 
    # then return true 
    if col >= N: 
        return True
  
    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(N): 
  
        if isSafe(board, i, col): 
              
            # Place this queen in board[i][col] 
            board[i][col] = 1
  
            # recur to place rest of the queens 
            if solveNQUtil(board, col + 1) == True: 
                return True
  
            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = 0
  
    # if the queen can not be placed in any row in 
    # this colum col then return false 
    return False
  
# This function solves the N Queen problem using 
# Backtracking. It mainly uses solveNQUtil() to 
# solve the problem. It returns false if queens 
# cannot be placed, otherwise return true and 
# placement of queens in the form of 1s. 
# note that there may be more than one 
# solutions, this function prints one of the 
# feasible solutions. 
def solveNQ(): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] ] 
  
    if solveNQUtil(board, 0) == False: 
        print ("Solution does not exist") 
        return False
  
    printSolution(board) 
    return True
  
# Driver Code 
solveNQ() 
  