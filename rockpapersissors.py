from tkinter import *
import tkinter.font as fn

window = Tk()

window.geometry('900x500')

fnt = fn.Font(family = 'Times New Roman', size = 14 )

window.config(bg = 'pale violet red')

window.title('Rock, Paper, Scissors!')

heading = Label(window, text = "ROCK, PAPER, SCISSORS!", font =('Times New Roman', 25, 'bold'), fg= 'maroon', bg = 'pale violet red' )
heading.grid(row = 0, column = 0, columnspan = 4, padx = 250)

result = Label(window)
result.grid(row = 1, column = 0, columnspan = 4, padx = 250)

option = Label(window, text = 'Your Option: ', font = fnt, fg= 'maroon', bg = 'pale violet red' )
option.grid(row = 2, column = 0, padx = 130)

rock = Button(window, bg = 'PaleVioletRed1', fg = 'PaleVioletRed4', text = 'Rock', font = fnt)
rock.grid(row = 2, column = 1)

paper = Button(window, bg = 'PaleVioletRed1', fg = 'PaleVioletRed4', text = 'Paper', font = fnt)
paper.grid(row = 2, column = 2)

scissors = Button(window, bg = 'PaleVioletRed1', fg = 'PaleVioletRed4', text = 'Scissors', font = fnt)
scissors.grid(row = 2, column = 3)

score = Label(window, text = 'Score: ', font = fnt, fg= 'maroon', bg = 'pale violet red' )
score.grid(row = 3, column = 0, padx = 130, pady = 20)

compsel = Label(window, text = 'Computer Selected: ' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
compsel.grid(row = 3, column = 1)
playsel = Label(window, text = 'Player Selected:' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
playsel.grid(row = 4, column = 1)
compscore = Label(window, text = 'Computer Score: ' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
compscore.grid(row = 3, column = 3)
playscore = Label(window, text = 'Player Score: ' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
playscore.grid(row = 4, column = 3)
window.mainloop()