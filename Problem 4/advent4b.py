import re

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

valid_passports = []
for i in range(len(input)):
	input[i] = [item for sublist in input[i] for item in sublist]
	for j in range(len(input[i])):
		input[i][j] = input[i][j].split(':')

	is_valid = True
	for j in range(len(input[i])):
		if input[i][j][0] == 'byr':
			if (len(input[i][j][1]) != 4 or 1920 > int(input[i][j][1]) or int(input[i][j][1]) > 2002):
				is_valid = False
				continue
		elif input[i][j][0] == 'iyr':
			if (len(input[i][j][1]) != 4 or 2010 > int(input[i][j][1]) or int(input[i][j][1]) > 2020):
				is_valid = False
				continue
		elif input[i][j][0] == 'eyr':
			if len(input[i][j][1]) != 4 or 2020 > int(input[i][j][1]) or int(input[i][j][1]) > 2030:
				is_valid = False
				continue
		elif input[i][j][0] == 'hgt':
			if 'in' in input[i][j][1]:
				height = int(input[i][j][1].split('in')[0])
				if 59 > height or height > 76:
					is_valid = False
					continue
			elif 'cm' in input[i][j][1]:
				height = int(input[i][j][1].split('cm')[0])
				if 150 > height or height > 193:
					is_valid = False
					continue
			else:
				is_valid = False
				continue
		elif input[i][j][0] == 'hcl':
			if not re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', input[i][j][1]):
				is_valid = False
				continue
		elif input[i][j][0] == 'ecl':
			if input[i][j][1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				is_valid = False
				continue
		elif input[i][j][0] == 'pid':
			if len(input[i][j][1]) is not 9 or not input[i][j][1].isnumeric():
				is_valid = False
				continue

	if is_valid:
		valid_passports.append(input[i])

valid_count = 0
for i in range(len(valid_passports)):
	avail_fields = []
	for j in range(len(valid_passports[i])):
		avail_fields.append(valid_passports[i][j][0])

	is_valid = True
	for field in fields:
		if field not in avail_fields:
			is_valid = False

	valid_count += 1 if is_valid else 0

print(valid_count)
