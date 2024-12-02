from tkinter import *
from tkinter import messagebox as mb

window = Tk()
window.geometry('900x500')
window.title('Welcome!')

mb.showinfo('Minecraft','Would you like to feed your animals? They seem hungry.')
mb.showwarning('Minecraft','Your animals WILL starve to death if you dont feed them right neow.')
mb.showerror('Error', 'Your laptop is malfunctioning.')
print(mb.askquestion('Food', 'Do you like food?'))
print(mb.askokcancel('Error', 'Would you like to share your social security number online?'))
print(mb.askyesno('No','Just pick one bruh i dont care'))
print(mb.askretrycancel('yes','yuh yuh'))


window.mainloop()