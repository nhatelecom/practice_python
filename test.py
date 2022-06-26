# rows, cols = 3,3
# my_matrix = [([0]*cols) for i in range(rows)]

# n=1
# for i in range(3):
#     for j in range(3):
#         my_matrix[i][j] = n
#         n+=1

# print(my_matrix)

# '''======='''


# # set_a = {1,2,2,3,2,4,4,5,7}

# # print(set_a)
# # print(len(set_a))

# # print("This is \x61 \ngood example")

# # print(r"This is \x61 \ngood example")

# '''-------------------------------------------------------------------------'''

# # import turtle
# # import math

# # r = int(input("Enter the radius: "))
# # t = turtle.Turtle()
# # t.hideturtle()
# # t.pensize(1)
# # t.color("red")
# # t.circle(r)
# # turtle.done()
# # c = 2 * math.pi * r
# # s = math.pi * r * r

# # print("Chu vi của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
# # print("Diện tích của hình tròn có bán kính = {r} là {s}".format(r=r, s=s))

# '''-------------------------------------------------------------------------'''


# # Import thư viện đồ họa turtle
# import turtle
# # Import thư viện sinh số ngẫu nhiên
# import random as r

# # khởi tạo turtle
# t = turtle.Turtle()
# t.shape("turtle")
# # Ẩn hình ảnh rùa
# t.hideturtle()
# t.pensize(3)
# t.color("blue")
# t.speed(1)
# t.penup()
# # Đặt vị trí ban đầu của con rùa sang bên trái
# # so với vị trí giữa màn hình 400 pixel
# # Mục đích để rùa chạy không ra khỏi màn hình
# # khi vòng lặp quá lớn
# t.goto(-400, 0)
# # Hiển thị hình ảnh con rùa
# t.showturtle()
# count = 0
# while count < 10:
#     # sinh hai giá trị ngẫu nhiên
#     down = r.randint(20, 50)
#     up = r.randint(20, 50)
#     t.pendown()
#     # rùa tiến về phía trước với giá trị ngẫu
#     # nhiên ở trên, có để lại nét vẽ
#     t.forward(down)
#     t.penup()
#     # rùa tiến về phía trước với giá trị ngẫu
#     # nhiên ở trên, không để lại nét vẽ
#     t.forward(up)
#     count += 1
# turtle.done()

'''-----------------------------------------------------------------'''

# # Import thư viện đồ họa turtle
# import turtle
# # Import thư viện sinh số ngẫu nhiên
# import random as r

# # Khởi tạo đối tượng turtle và đặt ví trí
# # con trỏ ở điểm 0, -200. Mục đích để vẽ
# # đường bao nhốt rùa cân chính giữa màn hình
# t = turtle.Turtle()
# # t.hideturtle()
# t.penup()
# t.goto(0, -200)

# # Vẽ đường bao nhốt rùa
# # đường bao có màu đen
# t.speed(2)
# t.pensize(10)
# t.pencolor("black")
# t.pendown()
# t.circle(200)

# # Đặt con trỏ rùa về chính giữa đường bao
# # Đổi màu rùa màu xanh
# t.penup()
# t.speed(10)
# t.shape("turtle")
# t.pencolor('green')
# t.goto(0, 0)

# # Tạo hướng ngẫu nhiên ban đầu cho rùa
# # khi ở vị trí chính giữa đường bao
# angle = r.randint(0, 360)
# t.right(angle)
# t.showturtle()

# # Bắt đầu cho rùa chạy thoát khỏi đường bao
# # Khi rùa di chuyển đến đường bao, bắt rùa
# # về lại vị trí chính giữa của hộp
# count = 0
# while True:
#     t.speed(1)
#     # rùa chỉ di chuyển một khoảng cách
#     # hơi bé hơn bán kính của hộp tròn là 200
#     # tránh rùa di chuyển đè lên vạch
#     t.forward(188)
#     # Bắt rùa về vị trí ban đầu, chính giữa hộp tròn
#     t.hideturtle()
#     t.speed(10)
#     t.goto(0, 0)
#     angle = r.randint(0, 360)
#     # Tạo hướng mới cho rùa chạy, thử vận may mới
#     t.right(angle)
#     t.showturtle()
#     # Khi rùa thử đến số lần nào đó thì dừng lại
#     # kết thúc chương trình bằng lệnh break
#     count += 1
#     if count == 10:
#         break

# turtle.done()

'''-----------------------------------------------------------'''

# import turtle
# import time
# r = 200

# # turtle.left(45)
# turtle.circle(r,90)    # Long curved part
# time.sleep(2)
# turtle.circle(r/3,90)  # Short curved part

# # turtle.left(45)
# # for loop in range(2):      # Draws 2 halves of ellipse
# #     turtle.circle(r,90)    # Long curved part
# #     turtle.circle(r/3,90)  # Short curved part

# turtle.exitonclick()

'''---------------------------------------------------'''
# import tkinter as tk

# window = tk.Tk()

# def save(event):
#     print("save pressed")
#     lbl.config(text="save pressed")

# def log(event):
#     print(event)
#     lbl2.config(text="logged")

# save_btn = tk.Button(window, text="Save")
# save_btn.pack()
# save_btn.bind("<Return>", save)
# # save_btn.bind("<Return>", log)
# save_btn.bind("<Return>", log, add= '+')

# lbl = tk.Label(window, text = '')
# lbl2 = tk.Label(window, text = '')
# lbl.pack()
# lbl2.pack()
# save_btn.focus()

# window.mainloop

'''---------------------------------------------------'''
# i = 0
# j = 20

# while True:
#     j -= 2
#     i += 3
#     if i >= j:
#         break
#     if j > 15:
#         continue
#     print(i, j, sep='', end='')
# else:
#     print(j, end='')
# print('a')

'''---------------------------------------------------------'''

