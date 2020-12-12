directions = []
for line in open('input.txt', 'r').readlines():
	readline = line.strip()
	directions.append((readline[0], int(readline[1:])))

compass = ['E', 'S', 'W', 'N']
direction = 0
x, y = 0, 0

direction_map = {
	'N': [0, 1],
	'S': [0, -1],
	'E': [1, 0],
	'W': [-1, 0],
}


def rotate(d, n, direction):
	direction += (- n // 90) if d == 'L' else n // 90
	return direction % 4


for d, n in directions:
	if d in ['N', 'S', 'E', 'W']:
		x += direction_map[d][0] * n
		y += direction_map[d][1] * n
	elif d in ['L', 'R']:
		direction = rotate(d, n, direction)
	elif d == 'F':
		x += direction_map[compass[direction]][0] * n
		y += direction_map[compass[direction]][1] * n

print(abs(x) + abs(y))
