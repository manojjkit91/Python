#Program To Multiply Two Matrix

matrix1 = [[9,8,7],[4,5,6],[3,2,1]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix1)):
	for j in range(len(matrix2[0])):
		for k in range(len(matrix2)):
			result[i][k] = matrix1[i][k] + matrix2[k][j]
for r in result:
	print(r)