cmds = []
for line in open('input.txt', 'r').readlines():
	cmd = line.strip().split()
	cmd[1] = int(cmd[1])
	cmds.append(cmd)


def process_cmd(acc, visited, i):
	if i in visited:
		return acc, 'Looped'
	cmd, val = cmds[i][0], cmds[i][1]
	visited.append(i)
	next_cmd = i + val if cmd == 'jmp' else i + 1
	acc += val if cmd == 'acc' else 0
	if i == len(cmds) - 1:
		return acc, 'Terminated'
	return process_cmd(acc, visited, next_cmd)


def swap_cmd(i):
	if cmds[i][0] == 'nop':
		cmds[i][0] = 'jmp'
	elif cmds[i][0] == 'jmp':
		cmds[i][0] = 'nop'


for i in range(len(cmds)):
	swap_cmd(i)
	acc, status = process_cmd(0, [], 0)
	if status == 'Terminated':
		print(acc, status)
		break
	swap_cmd(i)  # swap back
