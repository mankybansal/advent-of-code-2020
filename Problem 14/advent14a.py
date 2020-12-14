def apply_mask(mask, num):
	num = list(num)
	for i in reversed(range(36)):
		num[i] = '1' if mask[i] == '1' else '0' if mask[i] == '0' else num[i]
	return num


cur_mask = None
memory = {}
for line in open('input.txt', 'r').readlines():
	instruction = line.strip()
	if 'mask' in instruction:
		cur_mask = instruction[7:]
	elif 'mem' in instruction:
		inst = instruction.replace(' ', '').split('=')
		address = '{:036b}'.format(int(inst[0][4:len(inst[0]) - 1]))
		bin_num = '{:036b}'.format(int(inst[1]))
		memory[address] = ''.join(apply_mask(cur_mask, bin_num))

answer = 0
for mem, val in memory.items():
	answer += int(val, 2)
print(answer)
