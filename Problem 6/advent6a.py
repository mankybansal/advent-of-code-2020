count, fq_map = 0, {}
for line in open('input.txt', 'r').readlines():
	answers = line.strip()

	if answers == '':
		count += len(fq_map.keys())
		fq_map = {}
		continue

	for char in answers:
		fq_map[char] = fq_map[char] + 1 if char in fq_map else 1

print('Total:', count)
