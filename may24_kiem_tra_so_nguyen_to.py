# # Kiểm tra có phải số nguyên tố hay không
# import math

# numA = 4

# la_so_nguyen_to = 1

# mid_number = math.ceil(math.sqrt(numA))

# for i in range(2,mid_number+1):
#     if numA%i==0:
#         la_so_nguyen_to = 0

# if la_so_nguyen_to == 0:
#     print(numA,"không phải số nguyên tố")
# else:
#     print(numA,"là số nguyên tố")


# # In ra các số nguyên tổ trong khoảng a và b
# import math

# a = 10
# b = 101

# for i in range(a,b):
#     numA = i
#     la_so_nguyen_to = True
#     mid_number = math.ceil(math.sqrt(numA))

#     for j in range(2,mid_number+1):
#         if numA%j==0:
#             la_so_nguyen_to = False

#     if la_so_nguyen_to: # if it is True
#         print(numA)

#Nhập n, in ra n số Fibonacci

n = 10

fibo1 = 1
fibo2 = 1

if n == 1:
    print(fibo1)
elif n == 2:
    print(fibo1)
    print(fibo2)
else:
    print(fibo1)
    print(fibo2)
    for i in range(n-2):
        fibo3 = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo3
        print(fibo3)