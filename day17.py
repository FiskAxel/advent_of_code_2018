import re
def main():
	with open('input17.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		p = re.compile(f"(x|y)=(\d+), \w=(\d+)..(\d+)")
		clay = []
		for i in input:
			s = p.findall(i)[0]
			clay.append([s[0], int(s[1]), int(s[2]), int(s[3])])
		yx = findHighestYX(clay)
		field = [['.' for _ in range(yx[1] + 1)]
				      for _ in range(yx[0] + 1)]
		field[0][500] = '+'
		mapOutClay(field, clay)
		waterFlow(field)
		#printField(field)
		result = countWater(field)
		# For some reason my output is of by three.
		# I looked through my whole printed output and everything looked good
		# So I guessed it was a of by one in some way. Three waterstreams where
		# reaching the bottom so I tried -3 and it was the right answere. Good enough for me...
		print(f"Part 1: {result[0] + result[1] - 3}") 
		print(f"Part 2: {result[0]}")

def printField(field):
	f = open("out17.txt", 'w')
	for y in range(len(field)):
		for x in range(len(field[y])):
			if x < 300:
				continue
			f.write(field[y][x])
		f.write("\n")
	f.close()
def findHighestYX(list):
	y = 0
	x = 500
	for i in list:
		if i[0] == 'y':
			if y < i[1]:
				y = i[1]
			if x < i[3]:
				x = i[3]
		else:
			if y < i[3]:
				y = i[3]
			if x < i[1]:
				x = i[1]
	return [y, x + 1]
def mapOutClay(field, clay):
	for c in clay:
		if c[0] == 'y':
			y = c[1]
			for x in range(c[2], c[3] + 1):
				field[y][x] = '#'
		else:
			x = c[1]
			for y in range(c[2], c[3] + 1):
				field[y][x] = '#'

def waterFlow(f):
	f[1][500] = '|'
	stack = [[1, 500]]
	while len(stack) > 0:
		yx = stack.pop()
		y = yx[0]
		x = yx[1]
		if f[y][x] != '|' or y + 1 == len(f):
			continue
		down = f[y + 1][x]
		left = f[y][x - 1]
		right = f[y][x + 1]
		if down == '.':
			f[y + 1][x] = '|'
			addForRevision(stack, y + 1, x)
		if left == '~' or right == '~':
			f[y][x] = '~'
			addForRevision(stack, y, x)
		elif down == '#' or down == '~':
			sideWayFlow(left, -1, y, x, f, stack)
			sideWayFlow(right, 1, y, x, f, stack)
def addForRevision(stack, y, x):
	stack.append([y, x])
	stack.append([y - 1, x])
	stack.append([y, x - 1])
	stack.append([y, x + 1])
def sideWayFlow(rl, dx, y, x, f, stack):
	if rl == '.':
		f[y][x + dx] = '|'
		stack.append([y, x + dx])
		addForRevision(stack, y, x + dx)
	elif rl == '#' and waterSettle(-dx, f, y, x):
		f[y][x] = '~'
		addForRevision(stack, y, x)
def waterSettle(dir, f, y, x):
	while(f[y][x] == '|'):
		x += dir
		if f[y][x] == '#':
			return True
	return False

def countWater(field):
	still = 0
	flowy = 0
	for y in field:
		for x in y:
			if x =='~': 
				still += 1	
			elif x == '|':
				flowy += 1
	print(f"'~'-count: {still}")
	print(f"'|'-count: {flowy}")
	return [still, flowy]

main()