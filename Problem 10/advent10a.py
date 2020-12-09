adapters = []
for line in open('input.txt', 'r').readlines():
	adapters.append(int(line.strip()))

adapters = sorted(adapters)
device_joltage = adapters[-1] + 3
adapters.append(device_joltage)

joltage, one_diff, three_diff = 0, 0, 0

for adapter in adapters:
	if adapter - joltage == 1:
		one_diff += 1
	elif adapter - joltage == 3:
		three_diff += 1
	joltage = adapter

print(one_diff * three_diff)
