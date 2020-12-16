from collections import defaultdict

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

valid_tickets = []
for ticket in nearby_tickets:
	is_valid = True
	for value in ticket:
		is_value_valid = False
		for _, (r1_min, r1_max), (r2_min, r2_max) in rules:
			if r1_min <= value <= r1_max or r2_min <= value <= r2_max:
				is_value_valid = True
				break
		if not is_value_valid:
			is_valid = False
			break
	valid_tickets += [ticket] if is_valid else []

answers = defaultdict(list)
for i in range(len(valid_tickets[0])):
	values = [valid_tickets[j][i] for j in range(len(valid_tickets))]
	for r_name, (r1_min, r1_max), (r2_min, r2_max) in rules:
		is_valid_rule = True
		for v in values:
			if not (r1_min <= v <= r1_max or r2_min <= v <= r2_max):
				is_valid_rule = False
		answers[i] += [r_name] if is_valid_rule else []
sorted_keys = sorted(answers, key=lambda x: len(answers[x]))


def assign_rules(i=0, stack=[]):
	if i == 20:
		answer = 1
		for j, r_name in enumerate(stack):
			answer *= my_ticket[sorted_keys[j]] if 'departure' in r_name else 1
		print(answer)
		return
	for r_name in answers[sorted_keys[i]]:
		if r_name not in stack:
			assign_rules(i + 1, stack[:] + [r_name])


assign_rules()
