'''
Vẽ hình oval gần giống Ellipse
'''
import turtle as pen

pen.pensize(3)
pen.speed(10)

color_list = ["red", "orange", "yellow", "green", "blue", "cyan", "lightgreen", "turquoise", "skyblue", "white smoke", "grey", "black"]

r=100   #radius

for t in range(36): # vẽ 36 hình elip, mỗi elip nghiêng 10 độ
    pen.pencolor(color_list[(0+t)%len(color_list)]) #color_list có bao nhiêu màu thì nó sẽ dùng xoay vòng
    for i in range(2):
        pen.circle(r/2,90)
        pen.circle(r,90)
    pen.left(10)    # đặt bút nghiêng 10 độ để vẽ elip khác
    
pen.done()