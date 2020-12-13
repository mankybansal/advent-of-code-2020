lines = open('input.txt', 'r').readlines()
timestamp = int(lines[0].strip())
buses = lines[1].strip().split(',')

m, x = [], []
for i, bus in enumerate(buses):
	if bus == 'x':
		continue
	bus = int(bus)
	m.append(bus)
	x.append((bus - i) % bus)


def extended_euclidean(a, b):
	if a == 0:
		return b, 0, 1
	else:
		g, y, x = extended_euclidean(b % a, a)
		return g, x - (b // a) * y, y


def modinv(a, m):
	return extended_euclidean(a, m)[1] % m


def crt(m, x):
	while True:
		temp1 = modinv(m[1], m[0]) * x[0] * m[1] + modinv(m[0], m[1]) * x[1] * m[0]
		temp2 = m[0] * m[1]
		m, x = [temp2] + m[2:], [temp1 % temp2] + x[2:]
		if len(x) == 1:
			break
	return x[0]


print(crt(m, x))
