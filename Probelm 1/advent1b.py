file = open('input.txt', 'r')
Lines = file.readlines()

input = []

for line in Lines:
	input.append(int(line.strip().split(' ')[0]))

my_dict = {}

for i, num1 in enumerate(input):
	for j, num2 in enumerate(input):
		if i != j and num1 + num2 <= 2020:
			my_dict[num1+num2] = [i, j]

for i, num1 in enumerate(input):
	if 2020 - num1 in my_dict:
		print (num1, my_dict[2020-num1])






