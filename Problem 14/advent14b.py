import itertools


def combinations(pattern):
	replace = [['0', '1'] if (c == 'X') else c for c in pattern]
	return [''.join(lst) for lst in list(itertools.product(*replace))]


mask, memory, answer = None, {}, 0
for line in open('input.txt', 'r').readlines():
	inst, val = line.strip().replace(' ', '').split('=')
	if 'mask' in inst:
		mask = val
	elif 'mem' in inst:
		mem_add = '{:036b}'.format(int(inst[4:-1]))
		masked_mem_add = ''.join([mask[i] if mask[i] in ['1', 'X'] else mem_add[i] for i in range(36)])
		for address in combinations(masked_mem_add):
			memory[address] = int(val)
print(sum(memory.values()))
