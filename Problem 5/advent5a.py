highest = -1

for line in open('input.txt', 'r').readlines():
	ticket = line.strip()
	row = int(ticket[0:7].replace('F', '0').replace('B', '1'), 2)
	col = int(ticket[7:10].replace('L', '0').replace('R', '1'), 2)
	highest = max(highest, row * 8 + col)

print('Highest ID:', highest)
