from tkinter import *

window = Tk()
window.geometry('900x500')

window.title('frames')

a = Label(window, text = 'Chocos And Ice Creams', fg = 'black' )
a.pack(side = 'top')

topframe = Frame(window)
topframe.pack(side = 'top', pady = 10)
topbutton1 = Button(topframe, text = 'Vanilla')
topbutton1.pack(side = 'left')
topbutton2 = Button(topframe, text = 'Chocolate')
topbutton2.pack(side = 'left')
topbutton3 = Button(topframe, text = 'Cookies and Cream')
topbutton3.pack(side = 'left')
bottomframe = Frame(window)
bottomframe.pack(side = 'bottom', pady = 10)
downbutton1 = Button(bottomframe, text = 'Cake')
downbutton1.pack(side = 'bottom')
downbutton2 = Button(bottomframe, text = 'Tiramisu')
downbutton2.pack(side = 'bottom')
downbutton3 = Button(bottomframe, text = 'Ice Cream')
downbutton3.pack(side = 'bottom')

window.mainloop()