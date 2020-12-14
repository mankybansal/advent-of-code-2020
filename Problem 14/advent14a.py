mask, memory, answer = None, {}, 0
for line in open('input.txt', 'r').readlines():
	inst, val = line.strip().replace(' ', '').split('=')
	if 'mask' in inst:
		mask = val
	elif 'mem' in inst:
		mem_add = '{:036b}'.format(int(inst[4:-1]))
		num = '{:036b}'.format(int(val))
		masked_num = [mask[i] if mask[i] in ['1', '0'] else num[i] for i in range(36)]
		memory[mem_add] = int(''.join(masked_num), 2)
print(sum(memory.values()))
