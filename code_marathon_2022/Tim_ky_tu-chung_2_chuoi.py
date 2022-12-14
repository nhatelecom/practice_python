a = 'aabbccd'
b = 'abcaa4343ddddd'

count = 0
a_new= list(dict.fromkeys(a)) # xoá ký tự trùng nhau
b_new= list(dict.fromkeys(b)) # xoá ký tự trùng nhau

print(a)
print(a_new)

print(b)
print(b_new)

for i in range(len(a_new)):
    if a_new[i] in b:
        count += 1

print(count)

# return count