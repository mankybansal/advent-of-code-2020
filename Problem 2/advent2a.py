file = open('input.txt', 'r')
Lines = file.readlines()

count = 0
# Strips the newline character
for line in Lines:
	line_parts = line.strip().split(' ')
	rule_part = line_parts[0].split('-')

	min_rule = int(rule_part[0])
	max_rule = int(rule_part[1])
	password = line_parts[2]
	char = line_parts[1][0]
	char_count = password.count(char)

	if max_rule >= char_count >= min_rule:
		count += 1

print(count)
