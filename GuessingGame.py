from tkinter import *
from tkinter import messagebox as mb

def bob():
    name = Name.get()
    mb.showinfo('Can you...?', 'Well, ' + name + '. I am thinking for a number from 1 to 20. Do you think you can guess the number CORRECTLY????????????????????')

window = Tk()
window.geometry('500x400')
window.title('Welcome!')

heading = Label(window, text = 'Welcome....to literally the best game ever (no cap no gloating.)', font = ('TkDefaultFont',12))
heading.pack()

subheading = Label(window, text = 'And what might your beautiful name be? :')
subheading.pack()

Name = Entry(window)
Name.pack()

ok = Button(window, text = 'OK', command = bob)
ok.pack()



window.mainloop()