from tkinter import *
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

#pass the value of index to max also
def laggingDiagonalCheck(index,index_type,max):   #index_type=row|col
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
                for col in range(max,min-1):
                    if data_board[index][col]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                        else:
                            count=0
                    index+=1
            return False
  

def leadingDiagonalCheck(index,index_type,max):   #index_type=row|col
            count=0
            if index_type=="col":
                for row in range(max):
                    if data_board[row][index]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                    else:
                        count=0
                    index+=1
            else:
                for col in range(max):
                    if data_board[index][col]==current:
                        count+=1
                        if count>=win_moves:
                            return True
                        else:
                            count=0
                    index+=1
            return False
                


def checkDiagonals():
    max=size-1
    for i in range(size):
        if(laggingDiagonalCheck(i,"col",i)):
            return True
        elif(laggingDiagonalCheck(i,"row",i)):
            return True
        elif(leadingDiagonalCheck(i,"col",max-i)):
            return True
        elif(leadingDiagonalCheck(i,"row",max-i)):
            return True
    return False

def checkRows():
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
            


def checkColumns():
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
    if checkColumns():
        win=True
        print(current," player won!"," win is",win)
    elif checkRows():
        win=True
        print(current," player won!"," win is",win)
    elif checkDiagonals():
        win=True
        print(current," player won!"," win is",win)



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
for i in range(0,15):
    for j in range(0,15):
        board[i][j]= Button(root, text = "")
        board[i][j].row=i
        board[i][j].col=j
        board[i][j].configure(command=board[i][j].onClick,width=root_width,height=root_height)
        board[i][j].grid(column=j,row=i) # set Button grid

root.mainloop()  #render screen