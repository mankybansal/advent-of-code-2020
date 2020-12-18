import re


def evaluate(exp):
	while '+' in exp:
		exp = re.sub(r'(\d+) \+ (\d+)', lambda x: str(int(x[1]) + int(x[2])), exp)
	return eval(exp)


answer = 0
lines = ['(' + l.strip() + ')' for l in open('input.txt', 'r').readlines()]
for line in lines:
	while '(' in line:
		line = re.sub(r'\([^\(\)]+\)', lambda x: str(evaluate(x[0][1:-1])), line)
	answer += int(line)
print(answer)
