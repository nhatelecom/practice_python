l = 9
r = 33
count = 0

for i in range(l,r+1):
    string_num = str(i)
    # print(string_num[0])
    if string_num[0] == string_num[-1]:
        count +=1

print(count)
