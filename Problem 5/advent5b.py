seats = {}

for line in open('input.txt', 'r').readlines():
	ticket = line.strip()
	row = int(ticket[0:7].replace('F', '0').replace('B', '1'), 2)
	col = int(ticket[7:10].replace('L', '0').replace('R', '1'), 2)
	seats[row * 8 + col] = 1

for i in range(0, 836):
	if i not in seats.keys() and i > 10:
		print('Missing ID: ', i)
