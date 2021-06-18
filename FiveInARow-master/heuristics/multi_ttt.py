from tkinter import *
from copy import copy, deepcopy
from time import perf_counter
from typing import List
from matplotlib import colors
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from threading import Thread
import matplotlib.pyplot as plt
import time
from tkinter.font import Font

plt.style.use('dark_background')

#15x15 board
data_board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# board of buttons
board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#label board
label_board=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# data_board copy
data_board_copy=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
minmaxFinished=False
current="x"
size=3
canPlay=True
max_moves=size*size
win_moves=3
n_move=0
root_width=100
root_height=100
win=False
human="x"
ai="o"
depth=2
time_array=[0]
minmax_time_array=[0]
ab_moves_array=[0]
minmax_moves_array=[0]
eval_scores_array=[0]
ab_text="A-B-Prunning "
mm_text="Minimax "

x_color="#c327ab"
y_color="#ffc045"
ab_ni=0
minmax_ni=0


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
                for row in range(max+1):
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
    #print("is win called","current player is",current)
    if checkColumns(data_board,current):
        win=True
        #print(current," player won!"," win is",win)
    elif checkRows(data_board,current):
        win=True
        #print(current," player won!"," win is",win)
    elif checkDiagonals(data_board,current):
        win=True
        #print(current," player won!"," win is",win)
    if win==True:
        indicator_label.configure(text="{0} player won!".format(current))
    #print("game still continues")

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
                
#ordinary minmax
def ominimax(board,player):
    global minmax_ni
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
            minmax_ni+=1
            move=availMoves[i]
            board[move[0]][move[1]]=player
            #print("move played ",move,"by ", player)
            result=ominimax(board,nextPlayer)
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




def minimax(board,player,alpha,beta):
    global ab_ni
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
            ab_ni+=1
            move=availMoves[i]
            board[move[0]][move[1]]=player
            #print("move played ",move,"by ", player)
            result=minimax(board,nextPlayer,alpha=alpha,beta=beta)
            board[move[0]][move[1]]=0
            if player==ai:
                if result>best_score:
                    best_score=result
                    if best_score>alpha:
                        alpha=best_score
                    if alpha>=beta:
                        break
            else:
                if result<best_score:
                    best_score=result
                    if best_score<beta:
                        beta=best_score
                    if alpha>=beta:
                        break
        return best_score

def makeAiMove(best_move):
    global data_board,current
    #print(" make AI move, called from evalAB. best move is",best_move)
    board[best_move[0]][best_move[1]].configure(text=ai)
    #print("data_board configured")
    #label_board[best_move[0]][best_move[1]].configure(text=ai)
    data_board[best_move[0]][best_move[1]]=ai
    #print("data board changed")
    if ai=="x":
        board[best_move[0]][best_move[1]].configure(bg=x_color,fg="black")
        #label_board[best_move[0]][best_move[1]].configure(bg=x_color,fg="black")
    else:
        board[best_move[0]][best_move[1]].configure(bg=y_color,fg="black")
        #label_board[best_move[0]][best_move[1]].configure(bg=y_color,fg="white")
    #print("evalAB move completed")
    current=ai
    isWin()
    current=human

def makeMoveInLabelBoard(best_move):
    #global data_board
    ##print("inside make AI move. best move is",best_move)
    #board[best_move[0]][best_move[1]].configure(text=ai)
    #print("move in label called from eval minmax")
    label_board[best_move[0]][best_move[1]].configure(text=ai)
    #print("label_board configured")
    #data_board[best_move[0]][best_move[1]]=ai
    if ai=="x":
        #board[best_move[0]][best_move[1]].configure(bg=x_color,fg="black")
        label_board[best_move[0]][best_move[1]].configure(bg=x_color,fg="black")
    else:
        #board[best_move[0]][best_move[1]].configure(bg=y_color,fg="white")
        label_board[best_move[0]][best_move[1]].configure(bg=y_color,fg="black")
    #print("eval minmax move completed")

def evalplot(y1):  
    # the figure that will contain the plot
    fig = Figure(figsize = (6, 2), dpi = 100)
    
    # adding the subplot
    plot1 = fig.add_subplot(111,picker=True)
    # plotting the graph
    
    plot1.plot(y1,color="#ff004d")
    #plot1.plot(y2,Label="Minimax",color="#00fff5")
    plot1.set_xlabel("Moves")
    plot1.set_ylabel("AI evaluation score")
    plot1.legend(["Alpha-beta prunning","Minmax"],loc="upper left")
    plot1.set_title("AI score(+score favours player,-ve->AI)",color="#f6c90e")

    def update_annot(xdata,ydata,pos):
        annot.xy=pos
        #annot.y=pos[1]
        vis=annot.get_visible()
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()
        else:
            text =str(round(ydata))
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.4)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        return

    #print("sub plot object",plot1)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = root)  

    def onpick(event):
        #print(event)    
        xdata=event.mouseevent.xdata
        ydata=event.mouseevent.ydata
        pos=(xdata,ydata)
        #print("click loc",pos)
        update_annot(xdata=xdata,ydata=ydata,pos=pos)
        return
    
    canvas.mpl_connect('pick_event', onpick)
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=11,column=2*size+5,rowspan=8)
    annot = plot1.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)


def movesplot(y1,y2):  
    # the figure that will contain the plot
    fig = Figure(figsize = (6, 2), dpi = 100)
    
    # adding the subplot
    plot1 = fig.add_subplot(111,picker=True)
    # plotting the graph
    
    plot1.plot(y1,Label="Alpha-beta prunning",color="#ff004d")
    plot1.plot(y2,Label="Minimax",color="#00fff5")
    plot1.set_xlabel("Moves")
    plot1.set_ylabel("Number of moves evaluated")
    plot1.legend(["Alpha-beta prunning","Minmax"],loc="upper left")
    plot1.set_title("Number of moves calculated",color="#f6c90e")

    def update_annot(xdata,ydata,pos):
        annot.xy=pos
        #annot.y=pos[1]
        vis=annot.get_visible()
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()
        else:
            text =str(round(ydata))
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.4)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        return

    #print("sub plot object",plot1)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = root)  

    def onpick(event):
        #print(event)    
        xdata=event.mouseevent.xdata
        ydata=event.mouseevent.ydata
        pos=(xdata,ydata)
        #print("click loc",pos)
        update_annot(xdata=xdata,ydata=ydata,pos=pos)
        return
    
    canvas.mpl_connect('pick_event', onpick)
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=9,column=2*size+8,rowspan=8)
    annot = plot1.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)


def plot(y1,y2):  
    # the figure that will contain the plot
    fig = Figure(figsize = (6, 2), dpi = 100)
    
    # adding the subplot
    plot1 = fig.add_subplot(111,picker=True)
    # plotting the graph
    
    plot1.plot(y1,Label="Alpha-beta prunning",color="#ff004d")
    plot1.plot(y2,Label="Minimax",color="#00fff5")
    plot1.set_xlabel("No. of Moves")
    plot1.set_ylabel("Decision time in seconds")
    plot1.legend(["Alpha-beta prunning","Minmax"],loc="upper left")
    plot1.set_title("Time taken by AI to decide",color="#f6c90e")

    def update_annot(xdata,ydata,pos):
        annot.xy=pos
        #annot.y=pos[1]
        vis=annot.get_visible()
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()
        else:
            text =str(round(ydata,ndigits=2))+" s"
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.4)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        return

    #print("sub plot object",plot1)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = root)  

    def onpick(event):
        #print(event)    
        xdata=event.mouseevent.xdata
        ydata=event.mouseevent.ydata
        pos=(xdata,ydata)
        #print("click loc",pos)
        update_annot(xdata=xdata,ydata=ydata,pos=pos)
        return
    
    canvas.mpl_connect('pick_event', onpick)
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=0,column=2*size+8,rowspan=8)
    annot = plot1.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

def evaluateAB():
    global canPlay,ab_ni
    availMoves=getAvailMoves(data_board)
    #availMoves=sortMoves(availMoves,data_board,ai)
    board=deepcopy(data_board)
    best_score=-99
    best_move=None
    start=perf_counter()
    ab_label.configure(text="thinking...",bg="#ff004d",fg="white")
    for l in availMoves:
        #print("inside eval ab. avail moves are",availMoves)
        board[l[0]][l[1]]=ai
        #print("move played ",l," by O")
        result=minimax(board,human,-99,99)
        board[l[0]][l[1]]=0
        ab_ni+=1
        if result > best_score:
            best_move=l
            best_score=result
    end=perf_counter()
    ttaken=end-start
    time_array.append(ttaken)
    ab_moves_array.append(ab_ni)
    ab_ni=0
    ab_label.configure(text=ab_text,bg="black",fg="#ff004d")
    makeAiMove(best_move)
    #print("evaluate AB finished")
    canPlay=True
    #plot(y1=time_array,y2=minmax_time_array)

def evaluateMinMax():
    global canPlay,minmax_ni
    availMoves=getAvailMoves(data_board_copy)
    #availMoves=sortMoves(availMoves,data_board_copy,ai)
    board=deepcopy(data_board_copy)
    best_score=-99
    best_move=None
    start=perf_counter()
    mm_label.configure(text="thinking...",bg="#00fff5",fg="black")
    for l in availMoves:
        #print("inside play eval minmax. avail moves are",availMoves)
        board[l[0]][l[1]]=ai
        minmax_ni+=1
        #print("move played ",l," by O")
        result=ominimax(board,human)
        board[l[0]][l[1]]=0
        if result > best_score:
            best_move=l
            best_score=result
    end=perf_counter()
    ttaken=end-start
    minmax_time_array.append(ttaken)
    minmax_moves_array.append(minmax_ni)
    minmax_ni=0
    mm_label.configure(text=mm_text,bg="black",fg="#00fff5")
    makeMoveInLabelBoard(best_move)
    canPlay=True
    #print("evaluate minmax finished")
    #plot(y1=time_array,y2=minmax_time_array)


def playAi():
    global data_board_copy, minmaxFinished
    #print("AI thinking")
    data_board_copy=copy(data_board)
    p1=Thread(target=evaluateAB)
    p2=Thread(target=evaluateMinMax)
    p1.start()
    p2.start()
    """while(True):
        if(minmaxFinished and abFinished):
            #print("checking lock")
            break"""
    minmaxFinished=False
    plot(y1=time_array,y2=minmax_time_array)
    movesplot(y1=ab_moves_array,y2=minmax_moves_array)
    

def onClick(obj):                      #callback function for each button's click
    global current, n_move, canPlay
    #print("(",obj.row,",",obj.col,")","is clicked"," win is",win)
    if (win==False and data_board[obj.row][obj.col]==0 and canPlay):
        canPlay=False 
        data_board[obj.row][obj.col]=current
        obj.configure(text=current)
        label_board[obj.row][obj.col].configure(text=current)
        if current=="x":
            obj.configure(bg=x_color,fg="black")
            label_board[obj.row][obj.col].configure(bg=x_color,fg="black")
        else:
            obj.configure(bg=y_color,fg="black")
            label_board[obj.row][obj.col].configure(bg=y_color,fg="black")
        isWin()
        if current=="x":
            current="o"
        else:
            current="x"
        n_move+=1
        if(n_move>=max_moves):
            #print("draw")
            indicator_label.configure(text="Game drawn :|")
            #exit()
        if current==ai and win!=True:
            playAi()
            isWin()
            current=human
            n_move+=1
    

#refresh minmax board if it makes a different decision than minimax
def refresh():
    #print("refreshing board")
    for i in range(size):
        for j in range(size):
            if data_board[i][j]=="x":
                label_board[i][j].configure(text="x",bg=x_color)
            elif data_board[i][j]=="o":
                label_board[i][j].configure(text="o",bg=y_color)
            else:
                label_board[i][j].configure(text="",bg="#26282b")
 
  
root=Tk()
root.configure(bg="black")
root.title("Tic-Tac-Toe")
root.geometry('900x500')
root_width=2
##print(root_width)
root_height=2
current="x"
root.resizable(False,False)
Button.row=0
Button.col=0
Button.onClick=onClick

for i in range(0,size):
    for j in range(0,size):
        board[i][j]= Button(root, text = "",bg="#26282b")
        board[i][j].row=i
        board[i][j].col=j
        board[i][j].configure(command=board[i][j].onClick,width=root_width,height=root_height)
        board[i][j].grid(column=j,row=i) # set Button grid

for i in range(0,size):
    for j in range(0,3):
        l=Label(root,text="",width=root_width,height=root_height,bg="black")
        l.grid(column=size+j+1,row=i)

for i in range(0,size):
    for j in range(0,size):
        label_board[i][j]=Button(root,text="",width=root_width,height=root_height,bg="#26282b",command=refresh)
        label_board[i][j].grid(column=size+4+j,row=i)
ab_label=Label(root,text="A-B-Prunning",bg="black",fg="#ff004d")
ab_label.grid(column=0,row=size+1,columnspan=5)
mm_label=Label(root,text="Minimax",bg="black",fg="#00fff5")
mm_label.grid(column=size+4,row=size+1,columnspan=5)
#playAi()
#current="o"
#n_move+=1
font=Font(size=15)
indicator_label=Label(root,text="Please play on the left-side board.",bg="black",fg="#ffd700",font=font)
indicator_label.grid(column=0,row=5,columnspan=2*size+7)
plot(y1=time_array,y2=minmax_time_array)
movesplot(y1=ab_moves_array,y2=minmax_moves_array)
root.mainloop()  #render screen