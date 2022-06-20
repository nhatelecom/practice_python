from calendar import c


# Vẽ đường xoắn ốc
# Dừng lại khi khoảng cách từ điểm ban đầu đến điểm vẽ lớn hơn 1 số định trước

import turtle as pen

# height = 3600
# width = 3600
# screen = pen.Screen()
# screen.screensize(width, height)

pen.speed = 10
max_distance

d=0.5
while True:
    pen.forward(d)
    pen.left(15)
    print("d =",round(pen.distance(0,0),2))
    if pen.distance(0,0) > max_distance:
        break
    d += 0.5
    
pen.done()
pen.exitonclick()