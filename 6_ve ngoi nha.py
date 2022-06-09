# [Bài tập] Vẽ ngôi nhà mơ ước

import turtle as pen

pen.pensize(3)
pen.pencolor("red")
pen.speed(5)

pen.up()
pen.goto(-300,0)
pen.down()

for i in range(3):
    pen.forward(200)
    pen.right(90)
pen.forward(200)
pen.right(45)
pen.forward(141)
pen.right(90)
pen.forward(141)

pen.up()
pen.goto(200,200)
pen.down()

pen.circle(100)
