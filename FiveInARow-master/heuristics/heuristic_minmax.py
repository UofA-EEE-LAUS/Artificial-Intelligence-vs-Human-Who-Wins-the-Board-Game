from tkinter import *
from copy import deepcopy
from time import perf_counter

#15x15 board
data_board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# board of buttons
board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
current="x"
size=15
canPlay=True
max_moves=size*size
win_moves=5
n_move=0
root_width=None
root_height=None
win=False
human="x"
ai="o"
depth=2

def getReducedMoves(board):            #function returns list of relavant available moves
    availMoves=set()
    for i in range(size):
        for j in range(size):
            if board[i][j]!=0:
                for i2 in range(i-2,i+2):
                    if i2>=0 and i2<size:
                        for j2 in range(j-2,j+2):
                            if j2>=0 and j2<size and board[i2][j2]==0:
                                availMoves.add((i2,j2))
    return list(availMoves)


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

def evaluate_rows(row,col,player,board):
    if player=="x":
        opponent="o"
    else:
        opponent="x"
    #check row
    cont_count=0
    single_marks=0
    closed_one=0
    closed_two=0
    two_in_row=0
    closed_three=0
    three_in_row=0
    straight_fours=0
    four_in_row=0
    five_in_row=0
    start=False                         # cell index -1 is occupied by opponent?
    if (col-1)<0 or board[row][col-1]==opponent:
        start=True
    elif (row-1)>=0 and (col-1)>=0 and board[row-1][col-1]==player:
        return None
    for j in range(col,col+5,1):
        if j<size:
            if board[row][j]==player:
                cont_count+=1
            elif board[row][j]==opponent:
                    if start==True:
                        return None 
                    else:
                        if cont_count==1:
                            closed_one+=1
                            cont_count=0
                        elif cont_count==2:
                            closed_two+=1
                            cont_count=0
                        elif cont_count==3:
                            closed_three+=1
                            cont_count=0
                        elif cont_count==4:
                            four_in_row+=1
                            cont_count=0
                        elif cont_count==5:
                            five_in_row+=1
                            cont_count=0

            else:
                if cont_count==1:
                    single_marks+=1
                elif cont_count==2:
                    two_in_row+=1
                elif cont_count==3:
                    three_in_row+=1
                    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
                        }
                    return dt
                elif cont_count==4:
                    straight_fours+=1
                    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
                        }
                    return dt
                if single_marks==2:
                    single_marks=1
                    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
                        }
                    return dt
                cont_count=0

        else:
            if start==False:
                if cont_count==4:
                    straight_fours+=1
                    cont_count=0
    if cont_count==5:
        five_in_row+=1
    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
        }
    return dt


def evaluate_cols(row,col,player,board):
    if player=="x":
        opponent="o"
    else:
        opponent="x"
    #check row
    cont_count=0
    single_marks=0
    closed_one=0
    closed_two=0
    two_in_row=0
    closed_three=0
    three_in_row=0
    straight_fours=0
    four_in_row=0
    five_in_row=0
    start=False                         # cell index -1 is occupied by opponent?
    if (row-1)<0 or board[row-1][col]==opponent:
        start=True
    elif (row-1)>=0 and (col-1)>=0 and board[row-1][col-1]==player:
        return None
    for j in range(row,row+5,1):
        if j<size:
            if board[j][col]==player:
                cont_count+=1
            elif board[j][col]==opponent:
                    if start==True:
                        return None 
                    else:
                        if cont_count==1:
                            closed_one+=1
                            cont_count=0
                        elif cont_count==2:
                            closed_two+=1
                            cont_count=0
                        elif cont_count==3:
                            closed_three+=1
                            cont_count=0
                        elif cont_count==4:
                            four_in_row+=1
                            cont_count=0
                        elif cont_count==5:
                            five_in_row+=1
                            cont_count=0

            else:
                if cont_count==1:
                    single_marks+=1
                elif cont_count==2:
                    two_in_row+=1
                elif cont_count==3:
                    three_in_row+=1
                    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
                        }
                    return dt
                elif cont_count==4:
                    straight_fours+=1
                    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
                        }
                    return dt
                if single_marks==2:
                    single_marks=1
                    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
                        }
                    return dt
                cont_count=0

        else:
            if start==False:
                if cont_count==4:
                    straight_fours+=1
                    cont_count=0
    if cont_count==5:
        five_in_row+=1
    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
        }
    return dt

def evaluate_diags(row,col,player,board):
    
    if player=="x":
        opponent="o"
    else:
        opponent="x"

    cont_count=0
    single_marks=0
    closed_one=0
    closed_two=0
    two_in_row=0
    closed_three=0
    three_in_row=0
    straight_fours=0
    four_in_row=0
    five_in_row=0
    start=False
    canCheckLead=True
    canCheckLag=True
    #leading diagonal check
    j=col
    if (row-1)<0 or (col-1)<0 or board[row-1][col-1]==opponent:
        start=True
    elif (row-1)>=0 and (col-1)>=0 and board[row-1][col-1]==player:
        canCheckLead=False
    if canCheckLead:
        for i in range(row,row+5):
            if (i<size) and (j<size):
                if board[i][j]==player:
                    cont_count+=1
                elif board[i][j]==opponent:
                    if start==True:
                        break 
                    else:
                        if cont_count==1:
                            closed_one+=1
                            cont_count=0
                        elif cont_count==2:
                            closed_two+=1
                            cont_count=0
                        elif cont_count==3:
                            closed_three+=1
                            cont_count=0
                        elif cont_count==4:
                            four_in_row+=1
                            cont_count=0
                        elif cont_count==5:
                            five_in_row+=1
                            cont_count=0

                else:
                            if cont_count==1:
                                single_marks+=1
                            elif cont_count==2:
                                two_in_row+=1
                            elif cont_count==3:
                                three_in_row+=1
                            elif cont_count==4:
                                straight_fours+=1
                            if single_marks==2:
                                single_marks=1
                            cont_count=0

            else:
                if start==False:
                    if cont_count==4:
                        straight_fours+=1
                        cont_count=0
            j+=1

    if cont_count==5:
        five_in_row+=1

    dt={
                        "closed_one":closed_one,
                        "single_mark":single_marks,
                        "closed_two":closed_two,
                        "two_in_row":two_in_row,
                        "closed_three":closed_three,
                        "three_in_row":three_in_row,
                        "four_in_row":four_in_row,
                        "straight_fours":straight_fours,
                        "five_in_row":five_in_row
        }
        
    j=col
    #check lagging diagonal
    start=False
    cont_count=0
    single_marks=0
    closed_one=0
    closed_two=0
    two_in_row=0
    closed_three=0
    three_in_row=0
    straight_fours=0
    four_in_row=0
    five_in_row=0
    if (row-1)<0 or (col+1)>=size or board[row-1][col+1]==opponent:
        start=True
    elif (row-1)>=0 and (col+1)<size and board[row-1][col+1]==player:
        canCheckLag=False
    if canCheckLag:
        for i in range(row,row+5):
            if (i<size) and (j>=0):
                if board[i][j]==player:
                    cont_count+=1
                elif board[i][j]==opponent:
                    if start==True:
                        break 
                    else:
                        if cont_count==1:
                            closed_one+=1
                            cont_count=0
                        elif cont_count==2:
                            closed_two+=1
                            cont_count=0
                        elif cont_count==3:
                            closed_three+=1
                            cont_count=0
                        elif cont_count==4:
                            four_in_row+=1
                            cont_count=0
                        elif cont_count==5:
                            five_in_row+=1
                            cont_count=0

                else:
                            if cont_count==1:
                                single_marks+=1
                            elif cont_count==2:
                                two_in_row+=1
                            elif cont_count==3:
                                three_in_row+=1
                            elif cont_count==4:
                                straight_fours+=1
                            if single_marks==2:
                                single_marks=1
                            cont_count=0

            else:
                if start==False:
                    if cont_count==4:
                        straight_fours+=1
                        cont_count=0
            j-=1

    if cont_count==5:
        five_in_row+=1

    dt["closed_one"]+=closed_one
    dt["single_mark"]+=single_marks
    dt["closed_two"]+=closed_two
    dt["two_in_row"]+=two_in_row
    dt["closed_three"]+=closed_three
    dt["three_in_row"]+=three_in_row
    dt["four_in_row"]+=four_in_row
    dt["straight_fours"]+=straight_fours
    dt["five_in_row"]+=five_in_row
    return dt


def heuristic(player,board):
    w1=1
    w2=10
    w3=100
    w4=1000
    w5=10000
    w6=100000
    w7=1000000
    w8=10000000
    w9=1000000000 
    n1=0
    n2=0
    n3=0
    n4=0
    n5=0
    n6=0
    n7=0
    n8=0
    n9=0
    for i in range(size):
        for j in range(size):
            if board[i][j]==player:
                dt=evaluate_rows(i,j,player,board)
                if dt!=None:
                    n1+=dt["closed_one"]
                    n2+=dt["single_mark"]
                    n3+=dt["closed_two"]
                    n4+=dt["two_in_row"]
                    n5+=dt["closed_three"]
                    n6+=dt["three_in_row"]
                    n7+=dt["four_in_row"]
                    n8+=dt["straight_fours"]
                    n9+=dt["five_in_row"]
                dt=evaluate_cols(i,j,player,board)
                if dt!=None:
                    n1+=dt["closed_one"]
                    n2+=dt["single_mark"]
                    n3+=dt["closed_two"]
                    n4+=dt["two_in_row"]
                    n5+=dt["closed_three"]
                    n6+=dt["three_in_row"]
                    n7+=dt["four_in_row"]
                    n8+=dt["straight_fours"]
                    n9+=dt["five_in_row"]
                dt=evaluate_diags(i,j,player,board)
                if dt!=None:
                    n1+=dt["closed_one"]
                    n2+=dt["single_mark"]
                    n3+=dt["closed_two"]
                    n4+=dt["two_in_row"]
                    n5+=dt["closed_three"]
                    n6+=dt["three_in_row"]
                    n7+=dt["four_in_row"]
                    n8+=dt["straight_fours"]
                    n9+=dt["five_in_row"]
    rt=(n1*w1+n2*w2+n3*w3+n4*w4+n5*w5+n6*w6+n7*w7+n8*w8+n9*w9)
    return rt


def sortMoves(availMoves,board,player):
    hl=[]
    if ai=="x":
        opponent="o"
    else:
        opponent="x"
    for move in availMoves:
        board[move[0]][move[1]]=player
        heu=heuristic(ai,board)-heuristic(opponent,board)
        hl.append(heu)
        board[move[0]][move[1]]=0
    
    if player==ai:
        for i in range(len(availMoves)):
            for j in range(i+1,len(availMoves),1):
                if hl[i]<hl[j]:
                    tmp=hl[i]
                    hl[i]=hl[j]
                    hl[j]=tmp
                    tmp=availMoves[i]
                    availMoves[i]=availMoves[j]
                    availMoves[j]=tmp
    
    else:
        for i in range(len(availMoves)):
            for j in range(i+1,len(availMoves),1):
                if hl[i]>hl[j]:
                    tmp=hl[i]
                    hl[i]=hl[j]
                    hl[j]=tmp
                    tmp=availMoves[i]
                    availMoves[i]=availMoves[j]
                    availMoves[j]=tmp
    return availMoves
                

def minimax(board,player,current):
    availMoves=getReducedMoves(board)
    availMoves=sortMoves(availMoves,board,player)
    if (current+1)>=depth:
        if ai=="x":
            opponent="o"
        else:
            opponent="x"
        return (heuristic(ai,board)-heuristic(opponent,board))

    elif len(availMoves) == 0:         # if drawn, no reward
        return 0
    else:
        if player==ai:
            best_score=-9999999999
            nextPlayer=human
        else:
            best_score=9999999999
            nextPlayer=ai
        for i in range(len(availMoves)):
            move=availMoves[i]
            board[move[0]][move[1]]=player
            print("move played ",move,"by ", player)
            result=minimax(board,nextPlayer,current+1)
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
    availMoves=getReducedMoves(data_board)
    availMoves=sortMoves(availMoves,data_board,ai)
    board=deepcopy(data_board)
    best_score=-9999999999
    best_move=None
    start=perf_counter()
    for l in availMoves:
        print("inside play ai. avail moves are",availMoves)
        board[l[0]][l[1]]=ai
        print("move played ",l," by O")
        result=minimax(board,human,0)
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