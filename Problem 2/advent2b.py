file = open('input.txt', 'r')
Lines = file.readlines()

count = 0
# Strips the newline character
for line in Lines:
	line_parts = line.strip().split(' ')
	rule_part = line_parts[0].split('-')

	pos_1 = int(rule_part[0]) - 1
	pos_2 = int(rule_part[1]) - 1
	password = line_parts[2]
	char = line_parts[1][0]

	if (password[pos_1] == char and password[pos_2] != char) or (password[pos_1] != char and password[pos_2] == char):
		count += 1

print(count)
