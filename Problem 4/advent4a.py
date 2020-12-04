file = open('input.txt', 'r')
Lines = file.readlines()

input = [[]]

fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

count = 0
for line in Lines:
	read_line = line.strip()

	if read_line == '':
		count += 1
		input.append([])
		continue

	input[count].append(read_line.split(' '))

valid_count = 0

for i in range(len(input)):
	input[i] = [item for sublist in input[i] for item in sublist]
	for j in range(len(input[i])):
		input[i][j] = input[i][j].split(':')[0]

	is_valid = True
	for field in fields:
		if field not in input[i]:
			is_valid = False

	valid_count += 1 if is_valid else 0

print(valid_count)
