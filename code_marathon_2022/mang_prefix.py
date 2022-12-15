s = '1 2 3 4'

a_list = []
b_list = []
for i in range(len(s)):
    if i%2==0:
        a_list.append(int(s[i]))

sum = 0
for i in range(len(a_list)):
    sum += a_list[i]
    b_list.append(sum)