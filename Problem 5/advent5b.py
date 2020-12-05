input = []
for line in open('input.txt', 'r').readlines():
	input.append(line.strip())

seats = {}

for ticket in input:
	t, b, l, r = 0, 127, 0, 7
	for char in ticket:
		if char == 'F':
			b = (b - t) // 2 + t
		elif char == 'B':
			t = (b - t) // 2 + t + 1
		elif char == 'L':
			r = (r - l) // 2 + l
		elif char == 'R':
			l = (r - l) // 2 + l + 1
	seats[t * 8 + l] = 1

for i in range(0, 836):
	if i not in seats.keys() and i > 10:
		print('Missing ID: ', i)
