import tkinter as tk



def add_phonenumber_func():
    name = entry_name.get()
    phonenumber = entry_phonenumber.get()
    print(name,phonenumber)
    f = open("demofile3.txt", "a", encoding="utf-8")
    f.write(name)
    f.write(";")
    f.write(phonenumber)
    f.write("\n")
    f.close()


window = tk.Tk()
window.title("Tiêu đề")

frame = tk.Frame(window)
frame.place(
    relx=0.5,
    rely=0.2,
    anchor=tk.CENTER
)
window.geometry('400x600+1+1')


# Khai báo widget 
lbl_name = tk.Label(frame,text="Tên")
lbl_phonenumber = tk.Label(frame,text="Số điện thoại")
entry_name = tk.Entry(frame)
entry_phonenumber = tk.Entry(frame)
btn_add = tk.Button(frame,text="Thêm SĐT",command=add_phonenumber_func)

# Dựng layout

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
lbl_phonenumber.grid(row=1, column=0)
entry_phonenumber.grid(row=1, column=1)
btn_add.grid(row=2, column=0, columnspan=2)

window.mainloop()


