from collections import Counter

adapters = []
for line in open('input.txt', 'r').readlines():
	adapters.append(int(line.strip()))

adapters = sorted(adapters)
device_joltage = adapters[-1] + 3
adapters.append(device_joltage)

dp = Counter()
dp[0] = 1

for adapter in adapters:
	dp[adapter] = dp[adapter - 3] + dp[adapter - 2] + dp[adapter - 1]

print(dp[device_joltage])
