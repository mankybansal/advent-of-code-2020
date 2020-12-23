cup_n = 1_000_000
cups = list(map(int, "398254716")) + list(range(10, cup_n + 1))
cir = dict(zip(cups, cups[1:] + cups[:1]))

cup_cur = cups[0]
for i in range(10_000_000):
	cup_1, cup_2, cup_3 = cir[cup_cur], cir[cir[cup_cur]], cir[cir[cir[cup_cur]]]
	cir[cup_cur] = cir[cup_3]

	cup_dest = cup_cur - 1
	while cup_dest in [cup_1, cup_2, cup_3] or cup_dest < 1:
		cup_dest -= 1
		if cup_dest < 1:
			cup_dest = cup_n

	cir[cup_3], cir[cup_dest] = cir[cup_dest], cup_1
	cup_cur = cir[cup_cur]

print(cir[1] * cir[cir[1]])
