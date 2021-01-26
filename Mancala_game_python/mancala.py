from os import system, name 
from art import logo
board=['4','4','4','4','4','4','0','4','4','4','4','4','4','0']

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')

def printbrd(board):
    print('       '+'12' +'  '+'11'+'   '+'10' +'    '+'9'+'    '+'8'+'    '+'7')
    print('------------------------------------------------')
    print('       '+board[12] +'    '+board[11]+'    '+board[10] +'    '+board[9]+'    '+board[8]+'    '+board[7])
    print(board[13]+'                                        '+board[6])
    print('       '+board[0] +'    '+board[1]+'    '+board[2] +'    '+board[3]+'    '+board[4]+'    '+board[5])
    print('------------------------------------------------')
    print('       '+'0' +'    '+'1'+'    '+'2' +'    '+'3'+'    '+'4'+'    '+'5')


def isGameOver(l):
    return (all(v=='0' for v in l[0:6]) or all(v=='0' for v in l[7:12]))


def p1move(l):
    clear()
    printbrd(l)
    print()
    selected=int(input("player 1: move: (select a non empty pit from 0 to 5)"))
    if selected not in range(0,6) or l[selected]== '0' : 
        print("Invalid move")
        selected=int(input("player 1: re-enter move: (select a non empty pit from 0 to 5)"))
    
    pieces=int(l[selected])
    l[selected]='0'
    while pieces>=1:
        (selected)+=1
        if (selected)>=13:
            selected=0
        m=int(l[selected])
        m+=1
        l[selected]=str(m)
        pieces-=1
        if pieces==0 and selected==6:
            p1move(l)
        if pieces==0 and selected in range(0,6) and (l[selected]) =='1':
            k=int(l[6])
            k=k+int(l[12-selected])+int(l[selected])
            l[6]=str(k)
            (l[12-selected])='0'
            (l[selected])='0'


def p2move(l):
    clear()
    printbrd(l)
    print()
    selected=int(input("player 2: move: (select a non empty pit from 7 to 12)"))
    if selected not in range(7,13) or l[selected]== '0' : 
        print("Invalid move")
        selected=int(input("player 1: re-enter move: (select a non empty pit from 7 to 12)"))
    
    pieces=int(l[selected])
    l[selected]='0'
    while pieces>=1:
        (selected)+=1
        if (selected)>13:
            selected=0
        if selected==6:
            selected=7
        m=int(l[selected])
        m+=1
        l[selected]=str(m)
        pieces-=1
        if pieces==0 and selected==13:
            p2move(l)
        if pieces==0 and selected in range(7,13) and (l[selected]) =='1':
            k=int(l[13])
            k=k+int(l[12-selected])+int(l[selected])
            l[13]=str(k)
            (l[12-selected])='0'
            (l[selected])='0'
        

def main():
    print(logo)
    print("welcome to Mancala!\nA simple board game in which players move stones from one pit to another, in consecutive order, attempting to accumulate the maximum pieces in their respective stores.\nPlayer 1 store is on the right and player 2 store on the left of the board. When all the pits of any player are empty, the game is over.\nThe player having maximum stones in their store wins.\nIf the last stone enters in your own store, you get one additional move. \n\nHere's the twist: If the last stone enters one of your own empty pits, all the stones in the opponent's pit exactly above it are added to your store!\n\n")
    play= input("Enter 'Y' to start the game ").upper()
    if play=="Y":
        while(True):
            if not isGameOver(board):
                
                p1move(board)
                
                p2move(board)
                
            else:
                print("Scores:\nplayer 1: "+board[6]+"  player 2: "+board[13])
                if int(board[6])>int(board[13]):
                    print("Player 1 wins!")
                    break
                elif int(board[6])<int(board[13]):
                    print("Player 2 wins!")
                    break
                elif int(board[6])==int(board[13]):
                    print("Its a tie game!")
                    break


main()
