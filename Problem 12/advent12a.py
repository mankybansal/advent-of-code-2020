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


def rotate(action, value, direction):
	idx = [*directions].index(direction)
	idx += (-1 if action == 'L' else 1) * (value // 90)
	return [*directions][idx % 4]


direction = 'E'
x, y = 0, 0

for action, value in instructions:
	if action in [*directions]:
		x += directions[action][0] * value
		y += directions[action][1] * value
	elif action in ['L', 'R']:
		direction = rotate(action, value, direction)
	elif action == 'F':
		x += directions[direction][0] * value
		y += directions[direction][1] * value

print(abs(x) + abs(y))
