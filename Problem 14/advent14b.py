def combinations(pattern, i, result):
	if i == len(pattern):
		return result.add(''.join(pattern))
	if pattern[i] == 'X':
		for ch in "01":
			pattern[i] = ch
			combinations(pattern, i + 1, result)
			pattern[i] = 'X'
	else:
		combinations(pattern, i + 1, result)
	return result


def apply_mask(mask, num):
	num = list(num)
	for i in reversed(range(36)):
		num[i] = '1' if mask[i] == '1' else 'X' if mask[i] == 'X' else num[i]
	return num


cur_mask = None
memory = {}
for line in open('input.txt', 'r').readlines():
	instruction = line.strip()
	if 'mask' in instruction:
		cur_mask = instruction[7:]
	elif 'mem' in instruction:
		inst = instruction.replace(' ', '').split('=')
		bin_mem = '{:036b}'.format(int(inst[0][4:len(inst[0]) - 1]))
		bin_num = '{:036b}'.format(int(inst[1]))
		for address in combinations(apply_mask(cur_mask, bin_mem), 0, set()):
			memory[address] = bin_num

answer = 0
for mem, val in memory.items():
	answer += int(val, 2)
print(answer)
