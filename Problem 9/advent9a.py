nums = []
for line in open('input.txt', 'r').readlines():
	nums.append(int(line.strip()))

for i in range(25, len(nums)):
	five_nums = nums[i-25:i]
	is_fine = False
	for j in range(25):
		for k in range(25):
			if j != k and five_nums[j] + five_nums[k] == nums[i]:
				is_fine = True
				break
	if not is_fine:
		print(nums[i])

