# Nhập 1 chuỗi số nguyên, là độ cao của chồng gạch.
# Tính xem có bao nhiêu ô có thể chứa được nước khi đổ vào chồng gạch

# Thuật toán:
#     Tìm cột cao nhất bên trái: a
#     Tìm cột cao nhất bên phải: b
#     Chiều cao khối gạch tại vị trí i: c
#     Nếu (a-b)>c thì: Chiều cao nước chứa được tại cột thứ i là: min(a,b) - c
    

block = "211712"
highest_block_left_size = 0
highest_block_right_size = 0
block_height = 0

sum_water = 0

for i in range(1,len(block)-1):

    # tìm cột cao nhất bên trái
    highest_block_left_size = int(block[0])
    for j in range(i):
        if highest_block_left_size < int(block[j]):
            highest_block_left_size =int(block[j])

    # tìm cột cao nhất bên phải
    highest_block_right_size = int(block[-1])
    for j in range(i,len(block)):
        if highest_block_right_size < int(block[j]):
            highest_block_right_size = int(block[j])
    
    # tính lượng nước
    block_height = int(block[i])
    if min(highest_block_left_size,highest_block_right_size) >= block_height:
        sum_water = sum_water + min(highest_block_left_size,highest_block_right_size) - block_height

print(sum_water)