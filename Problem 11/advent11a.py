import copy

seats = []
for line in open('input.txt', 'r').readlines():
	seats.append(list(line.strip()))

m, n = len(seats), len(seats[0])
adjacent = [[1, 1], [-1, -1], [1, -1], [-1, 1], [1, 0], [0, 1], [-1, 0], [0, -1]]


def fill():
	seats_copy, count = copy.deepcopy(seats), 0
	for i in range(m):
		for j in range(n):
			occupied = adj_seats(i, j, seats_copy).count('#')
			if seats_copy[i][j] == 'L' and occupied == 0:
				seats[i][j] = '#'
			elif seats_copy[i][j] == '#' and occupied >= 4:
				seats[i][j] = 'L'
			count += 1 if seats[i][j] == '#' else 0
	return count


def adj_seats(i, j, seats):
	found_seats = []
	for x, y in adjacent:
		if 0 <= i + x < m and 0 <= j + y < n:
			found_seats.append(seats[i + x][j + y])
	return found_seats


old_count, new_count = 0, None
while old_count != new_count:
	old_count, new_count = new_count, fill()
print(new_count)
