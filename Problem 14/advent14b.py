import itertools


def combinations(pattern):
	replace = [['0', '1'] if (c == 'X') else c for c in pattern]
	return [''.join(lst) for lst in list(itertools.product(*replace))]


def apply_mask(mask, num):
	num = list(num)
	for i in range(len(num)):
		num[i] = mask[i] if mask[i] in ['1', 'X'] else num[i]
	return num


cur_mask, memory, answer = None, {}, 0
for line in open('input.txt', 'r').readlines():
	instruction = line.strip()
	if 'mask' in instruction:
		cur_mask = instruction[7:]
	elif 'mem' in instruction:
		inst = instruction.replace(' ', '').split('=')
		bin_mem = '{:036b}'.format(int(inst[0][4:len(inst[0]) - 1]))
		bin_num = '{:036b}'.format(int(inst[1]))
		for address in combinations(apply_mask(cur_mask, bin_mem)):
			memory[address] = bin_num

for mem, val in memory.items():
	answer += int(val, 2)
print(answer)
