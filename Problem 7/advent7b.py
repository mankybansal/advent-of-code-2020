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
			number_key = 0
			if split_rule[0] != 'no':
				number_key = int(split_rule[0])
			key = (number_key, split_rule[1] + split_rule[2])
			ad_list[master_key].append(key)

answers = []
for key in ad_list.keys():
	visited = [key]
	queue = []

	for sub_key in ad_list[key]:
		queue.append(sub_key[1])

	while len(queue) > 0:
		cur_key = queue.pop()
		if cur_key[1:] in visited:
			continue
		visited.append(cur_key[1:])
		if cur_key[1:] == 'shinygold':
			answers.append(key)

		if cur_key[1:] in ad_list:
			for new_key in ad_list[cur_key[1:]]:
				queue.append(new_key)

queue = ad_list['shinygold']


for i in range(len(queue)):
	key = queue[i][1]
	queue[i] = (queue[i][0], ad_list[queue[i][1]])
print(queue)

