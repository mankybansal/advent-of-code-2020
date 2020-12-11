import re

file = open('input.txt', 'r')
Lines = file.readlines()

input, count = [[]], 0
for line in Lines:
	read_line = line.strip()
	if read_line == '':
		count += 1
		input.append([])
		continue
	input[count].append(read_line.split(' '))


def validate_eyes(value, _key):
	return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_hair(value, _key):
	return re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', value)


def validate_year(year, key):
	year_range = [1920, 2002] if key == 'byr' else [2010, 2020] if key == 'iyr' else [2020, 2030]
	return len(year) == 4 and int(year) in range(year_range[0], year_range[1] + 1)


def validate_height(height, _key):
	unit = 'in' if 'in' in value else 'cm' if 'cm' in value else None
	height_range = [59, 76] if unit == 'in' else [150, 193] if unit == 'cm' else None
	return unit and int(height.split(unit)[0]) in range(height_range[0], height_range[1] + 1)


def validate_passport_number(pid, _key):
	return len(pid) == 9 and pid.isnumeric()


validation_schema = {
	'byr': validate_year,
	'iyr': validate_year,
	'eyr': validate_year,
	'hgt': validate_height,
	'hcl': validate_hair,
	'ecl': validate_eyes,
	'pid': validate_passport_number,
}

valid_count = 0
for i in range(len(input)):
	input[i] = [item for sublist in input[i] for item in sublist]

	avail_fields = []
	for j in range(len(input[i])):
		input[i][j] = input[i][j].split(':')
		avail_fields.append(input[i][j][0])

	is_valid = True
	for field in validation_schema.keys():
		is_valid = False if field not in avail_fields else is_valid
	if not is_valid:
		continue

	for [key, value] in input[i]:
		is_valid = False if key in validation_schema.keys() and not validation_schema[key](value, key) else is_valid

	valid_count += 1 if is_valid else 0

print(valid_count)
