from collections import defaultdict

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
	if is_valid:
		valid_tickets.append(ticket)

answers = defaultdict(list)
for i in range(len(valid_tickets[0])):
	values = [valid_tickets[j][i] for j in range(len(valid_tickets))]
	for rule_name, (r1_min, r1_max), (r2_min, r2_max) in rules:
		is_valid_rule = True
		for value in values:
			if not r1_min <= value <= r1_max and not r2_min <= value <= r2_max:
				is_valid_rule = False
		if is_valid_rule:
			answers[i].append(rule_name)
sorted_keys = sorted(answers, key=lambda x: len(answers[x]))


def assign_columns(i=0, stack=[]):
	if i == 20 and len(set(stack)) == 20:
		answer = 1
		for j, rule_name in enumerate(stack):
			if 'departure' in rule_name:
				answer *= my_ticket[sorted_keys[j]]
		print(answer)
		return
	for rule_name in answers[sorted_keys[i]]:
		if rule_name not in stack:
			assign_columns(i + 1, stack[:] + [rule_name])


assign_columns()
