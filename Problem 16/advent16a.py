lines, line_i = [l.strip() for l in open('input.txt', 'r').readlines()], 0
rules = []
for line_i, line in enumerate(lines):
	if not line:
		break
	r_name, r_range = line.replace(' ', '').split(':')
	r1, r2 = [list(map(int, x.split('-'))) for x in r_range.split('or')]
	rules.append((r_name, r1, r2))
my_ticket = list(map(int, lines[line_i + 2].strip().split(',')))
nearby_tickets = [list(map(int, l.split(','))) for l in lines[line_i + 5:]]

bad_values = []
for ticket in nearby_tickets:
	for value in ticket:
		is_valid = False
		for _, (r1_min, r1_max), (r2_min, r2_max) in rules:
			if r1_min <= value <= r1_max or r2_min <= value <= r2_max:
				is_valid = True
				break
		bad_values += [value] if not is_valid else []
print(sum(bad_values))
