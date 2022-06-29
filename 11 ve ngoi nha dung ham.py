# [Bài tập] Vẽ ngôi nhà mơ ước

import turtle as pen

def ve_ngoi_nha():
    for i in range(3):
        pen.forward(200)
        pen.right(90)
    pen.forward(200)
    pen.right(45)
    pen.forward(141)
    pen.right(90)
    pen.forward(141)
    pen.left(45)


pen.pensize(3)
pen.pencolor("red")
pen.speed(5)

# Vẽ ngôi nhà số 1
pen.up()
pen.goto(-300,0)
pen.down()
ve_ngoi_nha()

# Vẽ ngôi nhà số 2
pen.up()
pen.goto(200,0)
pen.down()
ve_ngoi_nha()

# Vẽ mặt trời
pen.up()
pen.goto(200,200)
pen.down()
pen.circle(100)

pen.done()