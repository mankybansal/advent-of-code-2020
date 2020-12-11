file = open('input.txt', 'r')
Lines = file.readlines()

input = []

for line in Lines:
	input.append(line.strip())

m, n = len(input), len(input[0])

tree_count = 0

right, down = 3, 1
while down < m:
	square = input[down][right % n]
	tree_count += 1 if square == '#' else 0
	right += 3
	down += 1

print(tree_count)
