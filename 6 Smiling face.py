# Smiling face

import turtle

#define pen size
turtle.pensize(5)

turtle.speed(10)
 
#define pen color
turtle.pencolor("green")

#for outer bigger circle
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)

#for eyes
#Màu nền mắt là màu đỏ
turtle.fillcolor ("purple")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
 
# khai bao bien eyesize lưu kích thước mắt
eye_size = 17.5
 
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()
 
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#for nose
turtle.penup ()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-30, steps=3)

# for smile
turtle.penup()
turtle.goto(-50, -70)
turtle.pendown()
turtle.right(90)
turtle.circle(50,180)
turtle.mainloop()
