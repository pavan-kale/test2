

 

def print_solution(board):
   
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def is_safe(board, row, col):
   
    for i in range(col):
        if board[row][i] == 1:
            return False

   
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

   
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    
    if col >= N:
        return True

    
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  

           
            if solve_nq_util(board, col + 1):
                return True

            board[i][col] = 0  

    return False  

def solve_nq():
   
    board = [[0] * N for _ in range(N)]  

    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True


N = 4 
solve_nq()
