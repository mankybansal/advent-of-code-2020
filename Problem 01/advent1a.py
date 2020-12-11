file = open('input.txt', 'r')
Lines = file.readlines()

input = []

for line in Lines:
	input.append(int(line.strip().split(' ')[0]))

my_dict = {}

for i, num in enumerate(input):
	my_dict[num] = i

for i, num in enumerate(input):
	if 2020 - num in my_dict:
		print (num, 2020-num)






