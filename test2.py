# from tkinter import *
# root = Tk()
# label = Label(text="hello")
# def change():
#     label["text"] = "world"
# button = Button(text="Change", command=change)
# label.pack()
# button.pack()

# root.mainloop()



import tkinter as tk

def command(event):
    print("hi")

root = tk.Tk()

label = tk.Label(text="Click me!", width=50, height=10, master=root)
label.pack()
label.bind("<Button-1>", command)

root.mainloop()
