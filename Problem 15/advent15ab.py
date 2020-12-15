from collections import defaultdict

numbers = [1, 0, 18, 10, 19, 6]
i, memory = 1, defaultdict(list)
for num in numbers:
	memory[num] = [i]
	i += 1

last_num = numbers[-1]
for i in range(i, 30000000 + 1):
	history = memory[last_num]
	last_num = 0 if len(history) == 1 else history[-1] - history[-2]
	memory[last_num].append(i)
	if i == 2020:
		print('Part A: ', last_num)
	if i == 30000000:
		print('Part B: ', last_num)
