# s = '13.5 4456.23423423 723424.12 234234.1 534234.432'
# x= '15.5'

s='22343534.12 42312312.13 7235345.154 0 -5'
x= '42312312.12'

num_list = s.split(' ')
print(num_list)

num_list = list(map(float, num_list))

for i in range(len(num_list)):
    if num_list[i]==int(num_list[i]):
        num_list[i] = int(num_list[i])

x = float(x)

# print(num_list)
# print(x)
# print(num_list[0])

distance_to_x = [abs(i-x) for i in num_list]

print(distance_to_x)

max_distance = num_list[distance_to_x.index(max(distance_to_x))]

print(max_distance)
# return max_distance