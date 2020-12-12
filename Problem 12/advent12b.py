directions = []
for line in open('input.txt', 'r').readlines():
	readline = line.strip()
	directions.append((readline[0], int(readline[1:])))

x, y = 0, 0
wx, wy = 10, 1

direction_map = {
	'N': [0, 1],
	'S': [0, -1],
	'E': [1, 0],
	'W': [-1, 0],
}


def rotate(d, n, wx, wy):
	steps = (- n // 90) if d == 'L' else n // 90
	if steps in [1, -3]:
		return wy, -wx
	if steps in [2, -2]:
		return -wx, -wy
	if steps in [3, -1]:
		return -wy, wx
	return wx, wy


for d, n in directions:
	if d in ['N', 'S', 'E', 'W']:
		wx += direction_map[d][0] * n
		wy += direction_map[d][1] * n
	elif d in ['L', 'R']:
		wx, wy = rotate(d, n, wx, wy)
	elif d == 'F':
		x += n * wx
		y += n * wy

print(abs(x) + abs(y))
