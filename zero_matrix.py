# Hàm tạo 1 ma trận 0 cỡ a nhân b
# Input: a và b là 2 chiều của ma trận
# Output: ma trận a*b toàn 0

def zero_matrix(a,b):
    matrix = []
    for i in range(a):
        matrix_temp = [0]*b
        matrix.append(matrix_temp)
    return matrix