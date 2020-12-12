instructions = []
for line in open('input.txt', 'r').readlines():
	readline = line.strip()
	instructions.append((readline[0], int(readline[1:])))

directions = {
	'E': [1, 0],
	'S': [0, -1],
	'W': [-1, 0],
	'N': [0, 1],
}
quad_signs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]


def rotate(action, value, wx, wy):
	quads = (-1 if action == 'L' else 1) * (value // 90)
	if quads % 2 != 0:
		wx, wy = wy, wx
	return wx * quad_signs[quads][0], wy * quad_signs[quads][1]


x, y = 0, 0
wx, wy = 10, 1

for action, value in instructions:
	if action in [*directions]:
		wx += directions[action][0] * value
		wy += directions[action][1] * value
	elif action in ['L', 'R']:
		wx, wy = rotate(action, value, wx, wy)
	elif action == 'F':
		x += value * wx
		y += value * wy

print(abs(x) + abs(y))
