def main():
	with open('input18.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		field = partOneSimulation(input, 10)
		print(f"Part 1: {count('|', field) * count('#', field)}")

		# Gets the 100 last resource values (out of 500)
		values = partTwoSimulation(input, 500) # Runs in about 1,5 minutes :/
		pattern = findPattern(values)
		patternStartMinute = values.index(pattern[0]) + 1 # Finds the minute the pattern starts.
		index = (1000000000 - (400 + patternStartMinute)) % len(pattern) - 1 # Index of the value for the 1000,000,000th minute.
		print(f"Part 2: {pattern[index]}")

def partOneSimulation(input, mins):
	field = []
	for y in input:
		row = []
		for x in y:
			if x == '\n':
				continue
			row.append(x)
		field.append(row)
	for m in range(mins):
		nf = [row[:] for row in field]
		for y in range(len(field)):
			for x in range(len(field)):
				if field[y][x] == '.': # Open
					if countAdjecents('|', field, y, x) >= 3:
						nf[y][x] = '|'
				elif field[y][x] == '|': # Trees
					if countAdjecents('#', field, y, x) >= 3:
						nf[y][x] = '#'
				elif field[y][x] == '#': # Lumberyard
					if countAdjecents('#', field, y, x) > 0 and countAdjecents('|', field, y, x) > 0:
						nf[y][x] = '#'
					else:
						nf[y][x] = '.'
		field = [row[:] for row in nf]
	return field
def partTwoSimulation(input, mins):
	field = []
	for y in input:
		row = []
		for x in y:
			if x == '\n':
				continue
			row.append(x)
		field.append(row)
	values = []
	for m in range(mins):
		nf = [row[:] for row in field]
		for y in range(len(field)):
			for x in range(len(field)):
				if field[y][x] == '.': # Open
					if countAdjecents('|', field, y, x) >= 3:
						nf[y][x] = '|'
				elif field[y][x] == '|': # Trees
					if countAdjecents('#', field, y, x) >= 3:
						nf[y][x] = '#'
				elif field[y][x] == '#': # Lumberyard
					if countAdjecents('#', field, y, x) > 0 and countAdjecents('|', field, y, x) > 0:
						nf[y][x] = '#'
					else:
						nf[y][x] = '.'
		field = [row[:] for row in nf]
		if m > mins - 100:
			values.append(count('|', field) * count('#', field))
	return values

def findPattern(values):
	for v in values:
		count = 0
		for vv in values:
			if vv == v:
				count += 1
		if count == 2:
			p1 = [v]
			p2 = [v]
			f = False
			s = False
			for vv in values:
				if f:
					p1.append(vv)
					s = True
				elif s:
					p2.append(vv)
					if vv == v:
						break
				if vv == v:
					f = not f
			if match(p1, p2):
				p1.pop()
				return p1
def match(p1, p2):
	for v, vv in zip(p1, p2):
		if v != vv:
			return False
	return True		

def printField(field):
	for y in field:
		for x in y:
			print(x, end="")
		print()
	print()
def count(t, field):
	count = 0
	for y in field:
		for x in y:
			if x == t:
				count += 1
	return count
def countAdjecents(t, field, y, x):
	trees = 0
	 # Starting top left
	y, x = y - 1, x - 1
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1
	x += 1
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1
	x += 1
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1

	y, x = y + 1, x - 2
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1
	x += 2
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1

	y, x = y + 1, x - 2
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1
	x += 1
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1
	x += 1
	if not outside(field, y, x) and field[y][x] == t:
		trees += 1

	return trees
def outside(field, y, x):
	if x < 0 or len(field) <= x:
		return True
	if y < 0 or len(field) <= y:
		return True
	return False

main()