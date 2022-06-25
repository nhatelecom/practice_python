import tkinter as tk

window = tk.Tk()

# # ! click
# def callback(event):
#     print("Clicked at", event.x, event.y)
#     label.config(text = "Clicked at " + str(event.x) + "-" + str(event.y))

# button = tk.Button(window, width=30, height=30, text = "Nút bấm")
# button.bind("<Button-1>", callback)
# button.pack()
# label = tk.Label(window, text="")
# label.pack()



'''=============================='''

# def save(event):
#     print("Save Button pressed")
#     lbl1.config(text="save pressed")
    
# def log(event):
#     print(event)
#     lbl2.config(text="logged")

# save_button = tk.Button(window, text="Save")
# save_button.pack()
# save_button.bind("<Return>", save)
# save_button.bind("<Return>", log, add='+')

# lbl1 = tk.Label(window, text = "")
# lbl2 = tk.Label(window, text = "")
# lbl1.pack()
# lbl2.pack()

# save_button.focus()

'''-------------------------------------------'''

username = "anhnh"
password = "123"

def login_btn_f():
    input_username = entry_user_name.get()
    input_password = entry_password.get()
    if input_username == username and input_password == password:
        lbl_message.text="Đăng nhập thành công"

login_frame = tk.Frame(window)
login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor=tk.CENTER
)

lbl_user_name = tk.Label(login_frame,text="User name: ")
lbl_password = tk.Label(login_frame,text="Password: ")
entry_user_name = tk.Entry(login_frame)
entry_password = tk.Entry(login_frame)

login_btn = tk.Button(
    login_frame,
    text="Login",
    command=login_btn_f)

lbl_message = tk.Label(login_frame,text="")

lbl_user_name.grid(row=0, column=0)
lbl_password.grid(row=1, column=0)
entry_user_name.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
login_btn.grid(row=2, column=0, columnspan=2)
lbl_message.grid(row=3, column=0, columnspan=2)





window.mainloop()
