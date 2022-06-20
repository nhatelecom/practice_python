rows, cols = 3,3
my_matrix = [([0]*cols) for i in range(rows)]

n=1
for i in range(3):
    for j in range(3):
        my_matrix[i][j] = n
        n+=1

print(my_matrix)

'''======='''


# set_a = {1,2,2,3,2,4,4,5,7}

# print(set_a)
# print(len(set_a))

# print("This is \x61 \ngood example")

# print(r"This is \x61 \ngood example")

'''-------------------------------------------------------------------------'''

# import turtle
# import math

# r = int(input("Enter the radius: "))
# t = turtle.Turtle()
# t.hideturtle()
# t.pensize(1)
# t.color("red")
# t.circle(r)
# turtle.done()
# c = 2 * math.pi * r
# s = math.pi * r * r

# print("Chu vi của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
# print("Diện tích của hình tròn có bán kính = {r} là {s}".format(r=r, s=s))

'''-------------------------------------------------------------------------'''
