board=[]

def resetbrd(board):
    for x in range(8):
        for y in range(8):
            board[x][y]=' '
        board[3][3]='X'
        board[3][4]='O'
        board[4][3]='O'
        board[4][4]='X'

        
def isValid(board,xst,yst):
    if not isOnBrd(xst,yst) or board[xst][yst]!=' ':
        return False
    else:
        return True


def printboard(board): 
    print("  0   1   2   3   4   5   6   7  ")
    for i in range(8):
        print('|   |   |   |   |   |   |   |   |  ')
        print('| '+board[i][0] +' | '+board[i][1]+' | '+board[i][2]+' | '+board[i][3] +' | '+board[i][4]+' | '+board[i][5]+' | '+board[i][6]+' | '+board[i][7]+' |   '+str(i))
        print('|   |   |   |   |   |   |   |   |  ')
        print("---------------------------------")

       
def isOnBrd(x,y) :
    return (x>=0 and x<=7 and y>=0 and y<=7)


def p1move(board):
        print("Player1: Enter your move:")
       
        xst=int(input("Row: "))
        yst=int(input("column: "))
        if not isValid(board,xst,yst):
            print("Enter a valid move..")
            p1move(board)
            
        else:    
    
            tile='X'
            Otile='O'
            board[xst][yst]=tile
            fliptiles=[]
            for xdir,ydir in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                x,y=xst,yst
                x+=xdir
                y+=ydir
                if not isOnBrd(x,y):
                    continue
                while board[x][y]==Otile:
                    x+=xdir
                    y+=ydir
                    if not isOnBrd(x,y):
                        break
                if not isOnBrd(x,y):
                    continue
                if board[x][y]==tile:
                    while True:
                        x-=xdir
                        y-=ydir
                        if x==xst and y==yst:
                            break
                        fliptiles.append([x,y])

            for x,y in fliptiles:
                board[x][y]=tile


def p2move(board):
        print("Player2: Enter your move:")
       
        xst=int(input("Row: "))
        yst=int(input("column: "))
        if not isValid(board,xst,yst):
            print("Enter a valid move..")
            p2move(board)
            
        else:    
    
            tile='O'
            Otile='X'
            board[xst][yst]=tile
            fliptiles=[]
            for xdir,ydir in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                x,y=xst,yst
                x+=xdir
                y+=ydir
                if not isOnBrd(x,y):
                    continue
                while board[x][y]==Otile:
                    x+=xdir
                    y+=ydir
                    if not isOnBrd(x,y):
                        break
                if not isOnBrd(x,y):
                    continue
                if board[x][y]==tile:
                    while True:
                        x-=xdir
                        y-=ydir
                        if x==xst and y==yst:
                            break
                        fliptiles.append([x,y])

            for x,y in fliptiles:
                board[x][y]=tile


def scores(board):
    score1=0
    score2=0
    for x in range(8):
        for y in range(8):
            if board[x][y]=='X':
                score1+=1
            if board[x][y]=='O':
                score2+=1
      
    printf("scores:   player1: "+str(score1)+"  player2: "+str(score2))
    if score1>score2:
        winner=player1
        printf("The WINNER is "+winner+" !!")
    elif score2>score1:
        winner=player2
        printf("The WINNER is "+winner+" !!")
    else:
        print("Its a TIE game!!")
    

def isGameOver(board):
    for x in range(8):
        for y in range(8):
            if board[x][y]==' ':
                return False
    else:
        return True

    
def main():
    print("Welcome to REVERSI\nPlayer1 symbol:X     Player2 symbol:O\n\n")
    for i in range(8):
        board.append([' ']*8)
    resetbrd(board)    
    printboard(board)
    while True:
        if isGameOver(board):
            print("GAME OVER!")
            scores(board)
            break
        p1move(board)
        printboard(board)
        p2move(board)
        printboard(board)
            
        

main()    
