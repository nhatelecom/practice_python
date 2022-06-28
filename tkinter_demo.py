import tkinter as tk


window = tk.Tk()
window.title("Tiêu đề cửa sổ aaa")
my_label = tk.Label(
    window,
    text = "test abc",
    bg = "pink",
    # width = 50,
    # height = 50,
    anchor = "n",
    justify= "right",
    
    padx = 100,
    pady = 100,
    # Tìm hiểu padding, border, margin
    relief="solid",

)
my_label.pack()

my_list = ["hs1","hs2","hs3","hs4","hs5"]

for i in range (len(my_list)):
    my_label2 = tk.Label(window, text = my_list[i],anchor="s").pack()

window.mainloop()