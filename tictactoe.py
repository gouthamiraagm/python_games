import numpy#its a 2D board
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
player1='X'
player2='O'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False
def check_column(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False
def check_diagonal(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol, 'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
         print(symbol, 'won')
         return True
    return False
    
def won(symbol):
    return check_rows(symbol) or check_column(symbol) or check_diagonal(symbol)
def place(symbol):  #checks the user enter position is valid one or not
    print(numpy.matrix(board))
    while(1):
        row=int(input('enter row - 1 or 2 or 3 :'))
        col=int(input('enter column - 1 or 2 or 3 :'))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print('Invalid input.please enter again')
    board[row-1][col-1]=symbol
def play(): #giving the turns even for x ,odd for o
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(player1)
            if won(player1):
                break
        else:
            print('O turn')
            place(player2)
            if won(player2):
                break
    if not(won(player1)) and not(won(player2)):
         print("draw")
play()
