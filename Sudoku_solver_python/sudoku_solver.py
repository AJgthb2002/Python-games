#solves sudoku puzzle in from file sudoku_data.txt

handle=open("sudoku_data.txt")

lst=[[int(x) for x in line.split()] for line in handle]
board=lst.copy()
masterset={1,2,3,4,5,6,7,8,9}

def repeat(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return True
    return False            


def disp_board(board):
    print("\n-----------------------------------")
    for i in range(0,9):
        for j in range(0,9):
            print(board[i][j],end=" | ")
        print("\n-----------------------------------")


def checkinRow(i,j):
    return masterset-set(board[i][j] for j in range(0,9))        


def checkinCol(i,j):
    temp=[]
    for x in range(9):
        temp.append(board[x][j])
    return masterset-set(temp)


def checkSquare(i,j):
    first=[0,1,2]
    second=[3,4,5]
    third=[6,7,8]
    locate_sq=[first, second, third]
    for s in locate_sq:
        if i in s:
            row=s
        if j in s:
            col=s
    temp=[]
    for r in row:
        for c in col:
            temp.append(board[r][c])
    return masterset- set(temp)


def get_poss_vals(i,j):
    poss_vals=list(checkSquare(i,j).intersection(checkinRow(i,j)).intersection(checkinCol(i,j)))
    return poss_vals


def solve(board):
    while(repeat(board)):
        for i in range(9):
            for j in range(9):

                if board[i][j]==0:
                    poss_vals=get_poss_vals(i,j)
                    row_poss=[]                            # checking in row
                    for y in range(9):
                        if y==j:
                            continue
                        if board[i][y]==0:
                            for val in get_poss_vals(i,y):
                                row_poss.append(val)
                    if len(set(poss_vals)-set(row_poss)) == 1:
                        board[i][j]=list(set(poss_vals)- set(row_poss))[0]
                        
                    col_poss=[]                            #checking in column
                    for x in range(9):
                        if x==i:
                            continue
                        if board[x][j]==0:
                            for val in get_poss_vals(x,j):
                                col_poss.append(val)
                    if len(set(poss_vals)-set(col_poss))==1:
                        board[i][j]=list(set(poss_vals)-set(col_poss))[0]
                        
                    #check in square
                    first=[0,1,2]
                    second=[3,4,5]
                    third=[6,7,8]
                    locate_sq=[first, second, third]
                    for s in locate_sq:
                        if i in s:
                            row=s
                        if j in s:
                            col=s
                    sq_poss=[]
                    for x in row:
                        for y in col:
                            if board[x][y]==0:
                                for val in get_poss_vals(x,y):
                                    sq_poss.append(val)

                    if len(set(poss_vals)- set(sq_poss))==1:
                        board[i][j]=list(set(poss_vals)- set(sq_poss))[0]               
    print("Solved : ")
    disp_board(board)

print("Sudoku puzzle:")
disp_board(board)
print("\n\n")
solve(board)

handle.close()            
