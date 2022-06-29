import tkinter as tk



def add_phonenumber_func():
    name = entry_name.get()
    phonenumber = entry_phonenumber.get()
    # lbl_msg_out.config(text='Bạn vừa thêm vào danh bạ:\n'+name+'-'+phonenumber)
    btn_2.config(text=name)
    
    
    # name = entry_name.get()
    # phonenumber = entry_phonenumber.get()
    # print(name,phonenumber)
    # f = open("demofile3.txt", "a", encoding="utf-8")
    # f.write(name)
    # f.write(";")
    # f.write(phonenumber)
    # f.write("\n")
    # f.close()

# def insert_info_from_dict(tk.Button(): button_clicked):
#     temp_text = button_clicked.cget('text')
#     print(temp_text)
#     # entry_msg_out.insert(0,temp_text)

def on_click(text):
    entry_name.delete(0,tk.END)
    entry_name.insert(0,text)


window = tk.Tk()
window.title("Tiêu đề")
# window.geometry("600x600")
window.resizable(width=0, height=0) #Không thay đổi được kích thước

frame = tk.Frame(window,height=400, width=400, bg="green")
# frame.place(
#     relx=0.5,
#     rely=0.5,
#     anchor=tk.CENTER
# )
frame.grid(row=0,column=0)

frame2 = tk.Frame(window,height=400, width=400, bg='pink')
frame2.grid(row=1,column=0)



# Khai báo widget 
lbl_name = tk.Label(frame,text='Tên')
lbl_phonenumber = tk.Label(frame,text="Điện thoại")
entry_name = tk.Entry(frame)
entry_phonenumber = tk.Entry(frame)
btn_add = tk.Button(frame,text='Thêm SĐT',command=add_phonenumber_func)


entry_name.insert(0,"Thử xem sao")
# Dựng layout

lbl_name.grid(row=0, column=0, sticky='e')
entry_name.grid(row=0, column=1)
lbl_phonenumber.grid(row=1, column=0)
entry_phonenumber.grid(row=1, column=1)
btn_add.grid(row=2, column=0, columnspan=2)

lbl_msg_out = tk.Label(frame2,text='')
lbl_msg_out.grid(row=0, column=0)

lbl_phonelist = tk.Label(frame2,text='Hoàng Ánh')
lbl_phonelist.grid(row=1, column=0)

btn_2 = tk.Button(frame2,text='',command= lambda: on_click (btn_2.cget('text')))
btn_2.grid(row=2, column=0)



print(lbl_phonelist.cget("text"))

window.mainloop()


