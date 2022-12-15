s = '1 2 3 3 4'

result = False

num_list = []
for i in range(len(s)):
    if i%2==0:
        num_list.append(int(s[i]))



for i in range(1,len(num_list)-1):
    left_sum = 0
    right_sum = 0
    # print("Mảng bên trái:")
    
    for j in range(i):
        # print(num_list[j],end=' ')
        left_sum = left_sum + num_list[j]
    # print(left_sum)
    
    for k in range(i+1,len(num_list)):
        # print(num_list[k],end=' ')
        right_sum = right_sum + num_list[k]
    # print(right_sum)

    if left_sum == right_sum:
        result = True
        break


print(result)