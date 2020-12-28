
def operations(matrix, num):	
	m = len(matrix)
	n = len(matrix[0])

	memory = [[[] for col in range(n)] for row in range (m)]
	memory[0][0].append(("", matrix[0][0]))

	for i in range(m):
		for j in range(n):
			if i != 0:
				for (path, sum) in memory[i-1][j]:
					memory[i][j].append((path+"D", sum+matrix[i][j]))
			if j != 0:
				for (path, sum) in memory[i][j-1]:
					memory[i][j].append((path+"R", sum+matrix[i][j]))

	for (path, sum) in memory[m-1][n-1]:
		if sum == num:
			return path

	return ""

def populate_matrix(m, n):
	return [[i+1]*m for i in range(n)]



#matrix_example = populate_matrix(4,4)

#print("operations for summmed 13: ", operations(matrix_example, 13))
#print("operations for summmed 16: ", operations(matrix_example, 16))
#print("operations for summmed 19: ", operations(matrix_example, 19))
#print('\n')

matrix_a = populate_matrix(9,9)

print("operations for summmed 65: ", operations(matrix_a, 65))
print("operations for summmed 72: ", operations(matrix_a, 72))
print("operations for summmed 90: ", operations(matrix_a, 90))
print("operations for summmed 110: ", operations(matrix_a, 110))
print('\n')

matrix_b = populate_matrix(90000,100000)

print("operations for summmed 87127231192: ", operations(matrix_a, 87127231192))
print("operations for summmed 5994891682: ", operations(matrix_a, 5994891682))