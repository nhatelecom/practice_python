import tkinter as tk


root = tk.Tk()
root.title("Chương trình quản lý thư viện v1.0 - (c) Nguyễn Hoàng Ánh 2022")
root.geometry("800x600")
root.resizable(width=0, height=0) #Không thay đổi được kích thước

button_frame = tk.Frame(root, bg='cyan', width = 100, height=600).grid(row=0, column=0)
# frame_button.pack()
openfile_btn = tk.Button(button_frame,text="Mở file",width = 12, height=2).grid(row=0, column=0, sticky=tk.NW)
booklist_btn = tk.Button(button_frame,text="Quản lý sách",width = 12, height=2).grid(row=0, column=0, sticky=tk.NW, pady = 50)
studentlist_btn = tk.Button(button_frame,text="Quản lý\n người mượn",width = 12, height=2).grid(row=0, column=0, sticky=tk.NW, pady = 100)
lend_management_btn = tk.Button(button_frame,text="Quản lý\n mượn sách",width = 12, height=2).grid(row=0, column=0, sticky=tk.NW, pady = 150)
savefile_btn = tk.Button(button_frame,text="Lưu file",width = 12, height=2).grid(row=0, column=0, sticky=tk.NW, pady = 200)

# openfile_btn.pack()
# booklist_btn.pack()


root.mainloop()