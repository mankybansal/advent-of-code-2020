input = []
for line in open('input.txt', 'r').readlines():
	input.append(line.strip())

highest = 0

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
	highest = max(highest, t * 8 + l)

print('Highest ID:', highest)
