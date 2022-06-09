# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# thisdict= dict()
# for i in range(len(color_name)):
#     thisdict[color_name[i]] = color_code[i]

# print(thisdict)


# # Bài 69
# my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new_list = list()

# for i in range(len(my_list)):
#     if my_list[i] not in new_list:
#         new_list.append(my_list[i])
            
# print(new_list)
# #===================================================================


# Xuất nhập ma trận

print("Nhập kích thước ma trận A (a*b)")
a = int(input("a = "))
b = int(input("b = "))

my_matrix = []

print("Nhập số liệu ma trận A")

for i in range(a):
    my_matrix_temp = []
    for j in range(b):
        my_matrix_temp.append(float(input("A["+str(i+1)+"]["+str(j+1)+"] = ")))
    my_matrix.append(my_matrix_temp)

print("Ma trận vừa nhập:")
for i in range(a):
    for j in range(b):
        print(my_matrix[i][j],"\t",end="")
    print("") # print \n