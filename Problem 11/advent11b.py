import copy

seats = []
for line in open('input.txt', 'r').readlines():
	seats.append(list(line.strip()))

m, n = len(seats), len(seats[0])
traverse = [[1, 1], [-1, -1], [1, -1], [-1, 1], [1, 0], [0, 1], [-1, 0], [0, -1]]


def fill():
	seats_copy, count = copy.deepcopy(seats), 0
	for i in range(m):
		for j in range(n):
			occupied = adj_seats(i, j, seats_copy).count('#')
			if seats_copy[i][j] == 'L' and occupied == 0:
				seats[i][j] = '#'
			elif seats_copy[i][j] == '#' and occupied >= 5:
				seats[i][j] = 'L'
			count += 1 if seats[i][j] == '#' else 0
	return count


def adj_seats(i, j, seats):
	found_seats = []
	for x, y in traverse:
		k = 1
		while 0 <= i + x * k < m and 0 <= j + y * k < n:
			if seats[i + x * k][j + y * k] in ['#', 'L']:
				found_seats.append(seats[i + x * k][j + y * k])
				break
			k += 1
	return found_seats


prev_count, curr_count = 0, None
while prev_count != curr_count:
	prev_count, curr_count = curr_count, fill()
print(curr_count)
