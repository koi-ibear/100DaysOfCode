"""1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""
def zeroMatrix(mat):
	rows = len(mat)
	if rows == 0:
		return None
	cols = len(mat[0])
	zero_row = set()
	zero_col = set()
	for r in range(rows):
		for c in range(cols):
			if mat[r][c] == 0:
				zero_row.add(r)
				zero_col.add(c)
	for r in zero_row:
		mat[r] = [0]*cols
	for c in zero_col:
		for i in range(rows):
			mat[i][c] = 0
	return mat


## test cases
mat0 = [[0]]

mat1 = [[1,0]]

mat2 = [[1,2,0,2],
		[2,1,1,0],
		[3,2,2,1]]

mat3 = [[1,2,3,0]]

for m in [mat0, mat1, mat2, mat3]:
	print('original')
	for i in m:
		print(i)
	print('updated')
	for i in zeroMatrix(m):
		print(i)