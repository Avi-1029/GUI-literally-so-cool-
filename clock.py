from tkinter import *
from time import strftime
import random

window = Tk()

window.title('clock!')

def time():
    tistr = strftime('%Y , %b , %d, %a  %I : %M : %S %p')
    clock.config(text = tistr)
    clock.after(1000, time)

def chcol():
    colours = ['Yellow','Orange','Green','Purple','Blue','Red','Violet','Light Blue','Teal']
    colors = ['snow','lavender','navy','olive drab','hot pink','gold','sky blue1']
    colour = random.choice(colours)
    color = random.choice(colors)
    clock.config(foreground= colour, background= color)
    clock.after(1000, chcol)

clock = Label(window, font= ('Times New Roman', 36), bg = 'gold', fg = 'white')
clock.pack(padx = 20, pady = 20)

time() 
chcol()
window.mainloop() 





