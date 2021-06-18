from tkinter import *
from copy import deepcopy
from time import perf_counter

#15x15 board
data_board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# board of buttons
board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
current="x"
size=3
canPlay=True
max_moves=size*size
win_moves=3
n_move=0
root_width=None
root_height=None
win=False
human="x"
ai="o"



def getAvailMoves(board):
    ls=[]
    for i in range(size):
        for j in range(size):
            if board[i][j]==0:
                t=(i,j)
                ls.append(t)
    return ls

#pass the value of index to max also
def laggingDiagonalCheck(index,index_type,max,data_board,current=current):   #index_type=row|col
            count=0
            if index_type=="col":
                for row in range(max):
                    if data_board[row][index]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                    else:
                        count=0
                    index-=1
            else:
                min=max
                max=size-1
                for col in range(max,min-1,-1):
                    if data_board[index][col]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                    else:
                        count=0
                    index+=1
            return False
  

def leadingDiagonalCheck(index,index_type,max,data_board,current=current):   #index_type=row|col
            count=0
            if index_type=="col":
                for row in range(max+1):
                    if data_board[row][index]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                    else:
                        count=0
                    index+=1
            else:
                for col in range(max+1):
                    if data_board[index][col]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                    else:
                        count=0
                    index+=1
            return False
                


def checkDiagonals(data_board,current=current):
    max=size-1
    for i in range(size):
        if(laggingDiagonalCheck(i,"col",i,data_board,current)):
            return True
        elif(laggingDiagonalCheck(i,"row",i,data_board,current)):
            return True
        elif(leadingDiagonalCheck(i,"col",max-i,data_board,current)):
            return True
        elif(leadingDiagonalCheck(i,"row",max-i,data_board,current)):
            return True
    return False

def checkRows(data_board,current=current):
    count=0
    for i in range(size):
        for j in range(size):
            if data_board[i][j]==current:
                count+=1
                if count>= win_moves:
                    return True
            else:
                count=0
        count=0
    return False
            


def checkColumns(data_board,current=current):
    count=0
    for i in range(size):
        for j in range(size):
            if data_board[j][i]==current:
                count+=1
                if count>= win_moves:
                    return True
            else:
                count=0
        count=0
    return False




def isWin():
    global win
    print("is win called","current player is",current)
    if checkColumns(data_board,current):
        win=True
        print(current," player won!"," win is",win)
    elif checkRows(data_board,current):
        win=True
        print(current," player won!"," win is",win)
    elif checkDiagonals(data_board,current):
        win=True
        print(current," player won!"," win is",win)
    print("game still continues")


def isWinPlayer(player,board):
    global win
    if checkColumns(board,player):
        return True
    elif checkRows(board,player):
        return True
    elif checkDiagonals(board,player):
        return True
    else:
        return False

def minimax(board,player):
    availMoves=getAvailMoves(board)
    if isWinPlayer(ai,board):            # if AI wins, AI gets maximum reward
        return 10
    elif isWinPlayer(human,board):       # if human wins, AI gets minimum reward
        return -10
    elif len(availMoves) == 0:         # if drawn, no reward
        return 0
    else:
        if player==ai:
            best_score=-99
            nextPlayer=human
        else:
            best_score=99
            nextPlayer=ai
        for i in range(len(availMoves)):
            move=availMoves[i]
            board[move[0]][move[1]]=player
            print("move played ",move,"by ", player)
            result=minimax(board,nextPlayer)
            board[move[0]][move[1]]=0
            if player==ai:
                #if result>=10:
                #    return result
                if result > best_score:
                    best_score=result
            else:
                #if result <=-10:
                #    return result
                if result<best_score:
                    best_score=result
        return best_score

def makeAiMove(best_move):
    global data_board
    print("inside make AI move. best move is",best_move)
    board[best_move[0]][best_move[1]].configure(text=ai)
    data_board[best_move[0]][best_move[1]]=ai

def playAi():
    print("AI thinking")
    availMoves=getAvailMoves(data_board)
    board=deepcopy(data_board)
    best_score=-99
    best_move=None
    start=perf_counter()
    for l in availMoves:
        print("inside play ai. avail moves are",availMoves)
        board[l[0]][l[1]]=ai
        print("move played ",l," by O")
        result=minimax(board,human)
        board[l[0]][l[1]]=0
        if result > best_score:
            best_move=l
            best_score=result
    end=perf_counter()
    ttaken=end-start
    print("time taken is",ttaken)
    makeAiMove(best_move)
    
    

def onClick(obj):                      #callback function for each button's click
    global current, n_move, canPlay
    print("(",obj.row,",",obj.col,")","is clicked"," win is",win)
    if (win==False and data_board[obj.row][obj.col]==0 and canPlay):
        canPlay=False 
        data_board[obj.row][obj.col]=current
        obj.configure(text=current)
        isWin()
        if current=="x":
            current="o"
        else:
            current="x"
        n_move+=1
        if(n_move>=max_moves):
            print("draw")
            exit()
        if current==ai and win!=True:
            playAi()
            isWin()
            current=human
            n_move+=1
    canPlay=True



root=Tk()
root.title="Five in a row"
root.geometry('500x650')
root_width=3
print(root_width)
root_height=2
current="x"
root.resizable(False,False)
Button.row=0
Button.col=0
Button.onClick=onClick
for i in range(0,size):
    for j in range(0,size):
        board[i][j]= Button(root, text = "")
        board[i][j].row=i
        board[i][j].col=j
        board[i][j].configure(command=board[i][j].onClick,width=root_width,height=root_height)
        board[i][j].grid(column=j,row=i) # set Button grid

root.mainloop()  #render screen