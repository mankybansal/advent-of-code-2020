from math import sin, cos, pi

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

x, y = 0, 0
wx, wy = 10, 1

for action, value in instructions:
	if action in [*directions]:
		wx += directions[action][0] * value
		wy += directions[action][1] * value
	elif action in ['L', 'R']:
		θ = (-1 if action == 'R' else 1) * value * pi / 180
		wx, wy = round(wx * cos(θ) - wy * sin(θ)), round(wx * sin(θ) + wy * cos(θ))
	elif action == 'F':
		x += value * wx
		y += value * wy

print(abs(x) + abs(y))
