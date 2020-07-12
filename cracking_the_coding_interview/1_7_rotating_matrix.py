"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
def rotateMatrix(mat):
	rows = len(mat)
	if rows < 1:
		return False
	cols = len(mat[0])
	if cols != rows:
		return False
	for layer in range(0, int(rows / 2)): ## if there are odd number of rows, the inner-most layer doesn't need to be rotated
		end = rows - layer - 1
		for i in range(layer, end):
			tmp = mat[layer][i] # tmp
			print(f"top from {mat[layer][i]}")
			mat[layer][i] = mat[rows-i-1][layer] # top = left
			print(f"to {mat[layer][i]}")
			print(f"left from {mat[rows-i-1][layer]}" )
			mat[rows-i-1][layer] = mat[end][rows-i-1] # left = bottom
			print(f"to {mat[rows-i-1][layer]}")
			print(f"bottom from {mat[end][rows-i-1]}" ) 
			mat[end][rows-i-1] = mat[i][end] # bottom = right
			print(f"to {mat[end][rows-i-1]}")
			print(f"right from {mat[i][end]}")
			mat[i][end] = tmp # right = top
			print(f"to {mat[i][end]}")
	return mat


## test cases
mat0 = [[0,1,2,3],
		[1,2,3,4],
		[2,3,4,5],
		[3,4,5,6]]

mat1 = [[0]]

mat2 = [[1,2,3,4,5,6,7],
		[7,6,5,4,3,2,1],
		[3,4,5,6,7,8,9],
		[9,8,7,6,5,4,3],
		[1,1,1,1,1,1,1],
		[0,0,0,0,0,0,0],
		[7,7,7,7,7,7,7]]
for i in rotateMatrix(mat0):
	print(i)

for i in rotateMatrix(mat1):
	print(i)

for i in rotateMatrix(mat2):
	print(i)		


