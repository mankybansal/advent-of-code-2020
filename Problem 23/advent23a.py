cup_n = 9
cups = list(map(int, "398254716"))
cir = dict(zip(cups, cups[1:] + cups[:1]))

cup_cur = cups[0]
for i in range(100):
	cup_1, cup_2, cup_3 = cir[cup_cur], cir[cir[cup_cur]], cir[cir[cir[cup_cur]]]
	cir[cup_cur] = cir[cup_3]

	cup_dest = cup_cur - 1
	while cup_dest in [cup_1, cup_2, cup_3] or cup_dest < 1:
		cup_dest -= 1
		if cup_dest < 1:
			cup_dest = cup_n

	cir[cup_3], cir[cup_dest] = cir[cup_dest], cup_1
	cup_cur = cir[cup_cur]

cur_cup = cir[1]
while cur_cup != 1:
	print(cur_cup, end='')
	cur_cup = cir[cur_cup]
