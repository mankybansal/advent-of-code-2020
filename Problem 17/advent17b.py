import copy

n = 40
grid = [[[['.' for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
grid[n // 2 - 1][n // 2 - 1] = [list(l.strip()) for l in open('input.txt', 'r').readlines()]

dirs = [(x, y, z, w) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1] for w in [-1, 0, 1]]
dirs.remove((0, 0, 0, 0))


def cycle():
	active_count = 0
	grid_copy = copy.deepcopy(grid)
	for x in range(n):
		print('-x', x)
		for y in range(n):
			for z in range(n):
				for w in range(n):
					neighbor_count = 0
					for dx, dy, dz, dw in dirs:
						if 0 <= x + dx < n and 0 <= y + dy < n and 0 <= z + dz < n and 0 <= w + dw < n:
							neighbor_count += 1 if grid_copy[x + dx][y + dy][z + dz][w + dw] == '#' else 0
					if grid_copy[x][y][z][w] == '#' and neighbor_count not in [2, 3]:
						grid[x][y][z][w] = '.'
					if grid_copy[x][y][z][w] == '.' and neighbor_count in [3]:
						grid[x][y][z][w] = '#'
					active_count += 1 if grid[x][y][z][w] == '#' else 0
	return active_count


count = None
for _ in range(6):
	count = cycle()
print(count)
