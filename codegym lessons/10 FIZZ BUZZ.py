'''
Mục tiêu:

Luyện tập sử dụng khối lệnh for và if…elif…else trong lập trình
Mô tả

Fizz Buzz là một bài toán lập trình cổ điển. Đây là phiên bản sửa đổi nhẹ của nó.
Viết chương trình lấy đầu vào là hai số nguyên: đầu và cuối khoảng (cả hai số đều thuộc khoảng).
Chương trình sẽ in ra các số trong khoảng này. Nhưng nếu số đó chia hết cho 3, bạn sẽ in ra “Fizz” thay vì nó, nếu số đó chia hết cho 5, in ra “Buzz” và nếu số đó chia hết cho cả 3 và 5, hãy in ra “FizzBuzz”.
'''

a=0
b=30

for i in range(a,b+1):
    if(i%3==0) and (i%5==0):
        print("FizzBuzz, ",end="")
    elif (i%3==0):
        print("Fizz, ",end="")
    elif (i%5==0):
        print("Buzz, ",end="")
    else:
        print(i,", ",end="")      
