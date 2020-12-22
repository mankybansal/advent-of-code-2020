lines = [l.strip() for l in open('input.txt', 'r').readlines()]

p1, p2, first_player = [], [], True
for line in lines:
	if 'Player 2' in line:
		first_player = False
	if not line or 'Player' in line:
		continue
	if first_player:
		p1.append(int(line))
	else:
		p2.append(int(line))

while len(p1) > 0 and len(p2) > 0:
	p1_card, p2_card = p1.pop(0), p2.pop(0)
	if p1_card > p2_card:
		p1 += [p1_card, p2_card]
	else:
		p2 += [p2_card, p1_card]

winner = p1 if len(p1) > 0 else p2
print(sum([(len(winner) - i) * card for i, card in enumerate(winner)]))
