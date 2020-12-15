def play_turns(turns):
	numbers, memory = [1, 0, 18, 10, 19, 6], {}
	for i in range(len(numbers)):
		memory[numbers[i]] = i + 1
	last_num = numbers[-1]
	for i in range(len(numbers) + 1, turns + 1):
		num = i - 1 - memory[last_num] if last_num in memory else 0
		memory[last_num] = i - 1
		last_num = num
	return last_num


print('Part A: ', play_turns(2020))
print('Part B: ', play_turns(30000000))
