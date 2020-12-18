import re


def evaluate(exp):
	result = int(exp[0])
	for i in range(1, len(exp)):
		if exp[i] == '+':
			i += 1
			result += int(exp[i])
		elif exp[i] == '*':
			i += 1
			result *= int(exp[i])
	return result


answer = 0
lines = ['(' + l.strip() + ')' for l in open('input.txt', 'r').readlines()]
for line in lines:
	while '(' in line:
		line = re.sub(r'\([^\(\)]+\)', lambda x: str(evaluate(x[0][1:-1].split())), line)
	answer += int(line)
print(answer)
