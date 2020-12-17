n = 8
grid = [[[['.' for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
grid[n // 2][n // 2] = [list(l.strip()) for l in open('input_v2.txt', 'r').readlines()]

dirs = [(x, y, z, w) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1] for w in [-1, 0, 1]]
dirs.remove((0, 0, 0, 0))


def cycle(i, n_new, new_grid):
	active_count = 0
	for x in range(n_new):
		for y in range(n_new):
			for z in range(n_new):
				for w in range(n_new):
					neighbor_count = 0
					for dx, dy, dz, dw in dirs:
						if 0 <= x + dx < n and 0 <= y + dy < n and 0 <= z + dz < n and 0 <= w + dw < n:
							neighbor_count += 1 if new_grid[x + dx][y + dy][z + dz][w + dw][i] == '#' else 0
					if new_grid[x][y][z][w][i] == '#':
						new_grid[x][y][z][w] += '.' if neighbor_count not in [2, 3] else '#'
					if new_grid[x][y][z][w][i] == '.':
						new_grid[x][y][z][w] += '#' if neighbor_count in [3] else '.'
					active_count += 1 if new_grid[x][y][z][w][i + 1] == '#' else 0
	return active_count


def increase_grid(i, n_old, old_grid):
	n_new = n_old + 2
	new_grid = [[[['.' * (i + 2) for _ in range(n_new)] for _ in range(n_new)] for _ in range(n_new)] for _ in
	            range(n_new)]
	for x in range(n_old):
		for y in range(n_old):
			for z in range(n_old):
				for w in range(n_old):
					new_grid[x + 1][y + 1][z + 1][w + 1] = old_grid[x][y][z][w]
	return n_new, new_grid


count = None
for i in range(6):
	count = cycle(i, n, grid)
	n, grid = increase_grid(i, n, grid)
print(count)
