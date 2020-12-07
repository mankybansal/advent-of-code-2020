ad_list = {}

for line in open('input.txt', 'r').readlines():
	rules = line.strip().replace('.', '').replace('contain', '').replace(',', ' ').split('  ')

	master_key = None
	for i in range(len(rules)):
		if i == 0:
			split_rule = rules[i].split(' ')
			key = split_rule[0] + split_rule[1]
			if key not in ad_list:
				ad_list[key] = []
			master_key = key
		else:
			split_rule = rules[i].split(' ')
			number_key = 0 if split_rule[0] == 'no' else int(split_rule[0])
			ad_list[master_key].append((number_key, split_rule[1] + split_rule[2]))


def recurse(key):
	if key == 'otherbags':
		return 0
	total = 0
	for q_num, q_key in ad_list[key]:
		total += (q_num * recurse(q_key)) + q_num
	return total


print(recurse('shinygold'))
