count, fq_map, curr_count = 0, {}, 0
for line in open('input.txt', 'r').readlines():
	answers = line.strip()

	if answers == '':
		for key in fq_map.keys():
			count += 1 if fq_map[key] == curr_count else 0
		fq_map, curr_count = {}, 0
		continue

	curr_count += 1

	for char in answers:
		fq_map[char] = fq_map[char] + 1 if char in fq_map else 1

print('Total:', count)
