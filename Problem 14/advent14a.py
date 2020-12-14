def apply_mask(mask, num):
	return ''.join([mask[i] if mask[i] in ['1', '0'] else num[i] for i in range(36)])


cur_mask, memory, answer = None, {}, 0
for line in open('input.txt', 'r').readlines():
	inst, val = line.strip().replace(' ', '').split('=')
	if 'mask' in inst:
		cur_mask = val
	elif 'mem' in inst:
		bin_mem = '{:036b}'.format(int(inst[4:-1]))
		bin_num = '{:036b}'.format(int(val))
		memory[bin_mem] = apply_mask(cur_mask, bin_num)

for mem, val in memory.items():
	answer += int(val, 2)
print(answer)
