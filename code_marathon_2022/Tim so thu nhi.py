# Tìm giá trị lớn nhất
# Lấy giá trị lớn nhất trừ cho tất cả giá trị trong list. KQ sẽ là dãy số không dương
# Tìm vị trí của số khác 0 và lớn nhất là được
 
s = '8 3 8 1 5 6 70'

num_list = s.split(' ')
num_list = list(map(int, num_list))

if len(num_list)==1:
    result = -1
elif len(num_list)==2 and num_list[0]==num_list[1]:
    result = -1
elif len(num_list)==2 and num_list[0]!=num_list[1]:
    result = num_list.index(min(num_list))
else:
    max_num = max(num_list)
    min_num = min(num_list)

    for i in range(len(num_list)):
        if num_list[i] == max_num:
            num_list[i] = min_num    
    
    result = num_list.index(max(num_list))

print(result)
# return result