rows, cols = 3,3
my_matrix = [([0]*cols) for i in range(rows)]

n=1
for i in range(3):
    for j in range(3):
        my_matrix[i][j] = n
        n+=1

print(my_matrix)