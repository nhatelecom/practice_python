s = '100 88 91'

num_list = s.split(' ')
num_list = list(map(int, num_list))
min_num = min(num_list)
max_num = max(num_list)

# print(min_num,max_num)

result_list = []
for i in range(min_num+1,max_num):
    if i not in num_list:
        result_list.append(i)
        # print(i)

print(result_list)
# return result_list

