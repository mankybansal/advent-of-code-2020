lines, line_i = open('input.txt', 'r').readlines(), 0
rules = []
for line_i in range(line_i, len(lines)):
	if lines[line_i].strip() == '':
		break
	rule_name, range_string = lines[line_i].strip().replace(' ', '').split(':')
	ranges = [list(map(int, x.split('-'))) for x in range_string.split('or')]
	rules.append((rule_name, ranges[0], ranges[1]))

my_ticket = list(map(int, lines[line_i + 2].strip().split(',')))

nearby_tickets = []
for line_i in range(line_i + 5, len(lines)):
	nearby_tickets.append(list(map(int, lines[line_i].strip().split(','))))

bad_values = []
for ticket in nearby_tickets:
	for value in ticket:
		is_valid = False
		for _, (r1_min, r1_max), (r2_min, r2_max) in rules:
			if r1_min <= value <= r1_max or r2_min <= value <= r2_max:
				is_valid = True
				break
		if not is_valid:
			bad_values.append(value)
print(sum(bad_values))
