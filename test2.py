from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Good morning :)')

frame1 = Frame(root, bg='green')
frame1.pack(expand=True, fill=BOTH)

button1 = Button(frame1, text='Hello1')
button1.pack(side=RIGHT)
button2 = Button(frame1, text='Hello2')
button2.pack(side=TOP)

root.mainloop()