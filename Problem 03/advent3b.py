file = open('input.txt', 'r')
Lines = file.readlines()

input = []

for line in Lines:
	input.append(line.strip())

m, n = len(input), len(input[0])

tree_product = 1
test_cases = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for right, down in test_cases:
	count = 0
	r, d = right, down
	while d < m:
		square = input[d][r % n]
		count += 1 if square == '#' else 0
		r += right
		d += down
	tree_product *= count

print(tree_product)
