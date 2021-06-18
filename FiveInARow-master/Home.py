from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk, Image
import sys
import os

root=Tk()
root.geometry('800x600')

# Welcome label
welcome = Label(root, text="Welcome!", padding=(30,20),font=("Helvetica", "16", "bold"))
welcome.pack()

#Select game
selectGame = Label(root, text="Select Game:", padding=(30,20), font=("Helvetica", "20", "bold"))
selectGame.pack()

#Function for play button
def playTicTacToe():
    #print("tic tac toe")
    global size
    size=3
    playButton.pack(pady=60)

def playFiveInARow():
    #print("Five in a row")
    selectDepth.pack()
    drop.pack()
    global size
    size=15
    playButton.pack(pady=60)

def play():
    #print(size)
    if size==3:
        root.destroy()
        os.system('python ./heuristics/multi_ttt.py')
    
    if size==15:
        root.destroy()
        #print("depth: "+str(clicked.get()))
        global depth
        depth=clicked.get()
        #path = 'python ./heuristics/heuristic_a_b.py '+str(depth)
        os.system("python ./heuristics/heuristic_a_b.py {depth}".format(depth=depth))

def getSize():
    #print(size)
    return size

def getDepth():
    return depth

#Button1
pic1 = Image.open("TicTacToe.jpg")
resized1 = pic1.resize((50,50), Image.ANTIALIAS)
newPic1 = ImageTk.PhotoImage(resized1)
Button(root, text = 'Tic Tac Toe', image = newPic1,
                    compound = LEFT, command=playTicTacToe).pack(side = TOP, pady=10)

#Button2
pic2 = Image.open("5inarow.png")
resized2 = pic2.resize((50,50), Image.ANTIALIAS)
newPic2 = ImageTk.PhotoImage(resized2)
Button(root, text = '5 in a row', image = newPic2,
                    compound = LEFT, command=playFiveInARow).pack(side = TOP, pady=10)


#Depth dropdown
selectDepth = Label(root, text="Select Depth:", padding=(30,20), font=("Helvetica", "12", "bold"))

options = ["0", "2", "4", "6"]
clicked = StringVar()
clicked.set( "2" )
drop = OptionMenu( root , clicked , *options)


#PlayButton
playButton = Button(root, text="Play", command=play, padding=(10,10))

mainloop()