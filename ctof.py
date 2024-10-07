from tkinter import *
import tkinter.font as fn

def cf():
    value = float(E.get())
    fahrenheit = value*9/5 + 32
    f.config(text = fahrenheit)


window = Tk()
window.geometry('900x500')
fnt = fn.Font(family = 'Comfortaa', weight = 'bold', size = 25)
window.title('Celsius and Fahrenheit Converter')

window.config(background= 'mistyrose')

C = Label(window, text = 'Temperature Converter', bg = 'mistyrose', fg = 'light coral', font = fnt)
C.pack(side = 'top')

fnt.configure(size = 12)
c = Label(window, text = 'Enter your Celsius Temperature:', bg = 'mistyrose', fg = 'black', font = fnt )
c.pack(side = 'top', pady = 10)

E = Entry(window)
E.pack(side = 'top', padx = 30, pady = 10)

show = Button(window, text = 'Convert', bg = 'light coral' , fg = 'white', command = cf)
show.pack(side = 'top', pady = 10)

f = Label(window, bg = 'mistyrose', fg = 'black', font = fnt )
f.pack(side = 'top', pady = 10)

window.mainloop()