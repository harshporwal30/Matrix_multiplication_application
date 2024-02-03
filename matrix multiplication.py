matrix1 = [[1,2, 3], [3,4, 9], [12,13,14]]
matrix2= [[5,6, 10], [7,8, 11], [15,16,17]]

result= [[0,0, 0], 
         [0,0, 0], 
         [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        for k in range(len(matrix2[0])):
            result[i][j] = result[i][j]+ (matrix1[i][k] * matrix2[k][j])
            
print("Matrix1 * Matrix2 = ")
for row in result:
    print(row)