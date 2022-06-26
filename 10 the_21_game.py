
'''
Mô tả: Trò chơi 21 là trò chơi số đếm được bắt đầu từ 0, hai người chơi lần lượt có thể thêm 1, 2 hoặc 3, vào tổng số. 
Tổng số không được vượt quá 21 và người chơi đếm tới 21 sẽ thua. Ở bài tập này, chúng ta sẽ giả định cho máy làm người chơi thứ 2.
'''

import random as r

current_sum = 0 


print("Bắt đầu chơi!")
while True:
    add_number = int(input("Người chơi chọn số (1-3): "))
    current_sum += add_number
    print("Tổng hiện tại =", current_sum)
    if (current_sum>=21):
        print("Người chơi đã thua")
        break

    add_number = r.randint(1,3)
    print("Máy đã chọn số:",add_number)
    current_sum += add_number
    print("Tổng hiện tại =", current_sum)
    if (current_sum>=21):
        print("Máy đã thua")
        break
    