lines = open('input.txt', 'r').readlines()
timestamp = int(lines[0].strip())
buses = lines[1].strip().split(',')

max_bus, max_time = None, float('inf')
for i, bus in enumerate(buses):
	if bus == 'x':
		continue
	bus = int(bus)
	if bus - (timestamp % bus) < max_time:
		max_bus, max_time = bus, (timestamp % bus)
print(max_bus * (max_bus - max_time))
