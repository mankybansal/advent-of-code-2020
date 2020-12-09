nums = []
for line in open('input.txt', 'r').readlines():
	nums.append(int(line.strip()))

num = 1930745883

for i in range(len(nums)):
	for j in range(i, len(nums)):
		cur_sum = sum(nums[i:j])
		if cur_sum == num and j - i > 2:
			print(min(nums[i:j]) + max(nums[i:j]))
		if cur_sum > num:
			break

