# s = '1 5 5 0 9 9 4 9'
s = '1 2 2 0 1 3 0 4'

num_list = []
for i in range(len(s)):
    if i%2==0:
        num_list.append(int(s[i]))


count_list = [0]* len(num_list)
# print(count_list)

for i in range(len(num_list)):
    for j in range(len(num_list)):
        if num_list[i] == num_list[j]:
            count_list[i] += 1

print(count_list)

result = True
for i in range(len(count_list)-1):
    for j in range(1,len(count_list)):
        if count_list[i] != count_list[j]:
            result = False
            break

print(result)