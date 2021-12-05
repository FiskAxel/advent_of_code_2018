class fighter:
	def __init__(s, y, x, atk):
		s.y = y
		s.x = x
		s.atk = atk
		s.hp = 200
	
walls = []
elves = []
goblins = []	

def main():
	with open('input15.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		initializeField(input, 3)
		print(f"Part 1: {battle(False)}") # 182376 	# old 185472
		
		elfAtk = 4
		while True:
			initializeField(input, elfAtk)
			result = battle(True)
			if result:
				break
			elfAtk += 1
		print(f"Part 2: {result}")  # 57540

def initializeField(input, elfAtk):
	global walls
	global elves
	global goblins
	walls = []
	elves = []
	goblins = []
	for y in range(len(input)):
		for x in range(len(input[y])):
			if input[y][x] == '#':
				walls.append([y, x])
			elif input[y][x] == 'E':
				elves.append(fighter(y, x, elfAtk))
			elif input[y][x] == 'G':
				goblins.append(fighter(y, x, 3))
def battle(part2):
	rounds = 0
	while len(elves) > 0 and len(goblins) > 0:
		rounds += 1
		fighters = elves.copy()
		fighters.extend(goblins)
		fighters.sort(key=lambda i: i.x)
		fighters.sort(key=lambda i: i.y)
		i = 0
		while i < len(fighters):
			if len(elves) == 0 or len(goblins) == 0:
				rounds -= 1
				break

			f = fighters[i]
			if f in goblins: 
				mates, targets = goblins, elves
			else: 
				mates, targets = elves, goblins

			if not targetInRange(f, targets, []):
				move = towardsClosestTarget(f, targets, mates)
				if move != None:
					f.y = move[0]
					f.x = move[1]
			target = []		
			if targetInRange(f, targets, target):
				target[0].hp -= f.atk
				if target[0].hp <= 0:
					if part2 and target[0] in elves:
						return False
					targets.remove(target[0])
					fighters.remove(target[0])
					if i < len(fighters) and f != fighters[i]:
						i -= 1
			i += 1
	hpSum = 0
	for f in fighters:
		hpSum += f.hp
	return rounds * hpSum

class queItem:
	def __init__(s, steps, y, x, yStepOne, xStepOne):
		s.steps = steps
		s.y = y
		s.x = x
		s.yStepOne = yStepOne
		s.xStepOne = xStepOne
def towardsClosestTarget(f, targets, mates):
	inRange = []
	visited = [f.y, f.x]
	que = [queItem(0, f.y, f.x, 0, 0)]
	for q in que:
		if targetInRange(fighter(q.y, q.x, 0), targets, []):
			inRange.append(q)
		elif len(inRange) == 0:
			appendIfOk(queItem(q.steps + 1, q.y - 1, q.x, q.yStepOne, q.xStepOne), que, visited, mates) # UP
			appendIfOk(queItem(q.steps + 1, q.y, q.x - 1, q.yStepOne, q.xStepOne), que, visited, mates) # LEFT
			appendIfOk(queItem(q.steps + 1, q.y, q.x + 1, q.yStepOne, q.xStepOne), que, visited, mates) # RIGHT
			appendIfOk(queItem(q.steps + 1, q.y + 1, q.x, q.yStepOne, q.xStepOne), que, visited, mates) # DOWN
	if len(inRange) > 0:
		inRange.sort(key=lambda i: i.xStepOne)
		inRange.sort(key=lambda i: i.yStepOne)
		inRange.sort(key=lambda i: i.x)
		inRange.sort(key=lambda i: i.y)
		inRange.sort(key=lambda i: i.steps)
		return [inRange[0].yStepOne, inRange[0].xStepOne]
def appendIfOk(q, que, visited, mates):
	if q.steps == 1:
		q.yStepOne = q.y
		q.xStepOne = q.x
	pos = [q.y, q.x]
	if pos in walls or pos in visited or positionIn(mates, pos):
		return
	visited.append(pos)
	que.append(q)
def targetInRange(f, targets, target):
	for t in targets:
		if abs(f.y - t.y) + abs(f.x - t.x) == 1:
			target.append(t)
	if len(target) > 0:
		target.sort(key=lambda i: i.x)
		target.sort(key=lambda i: i.y)
		target.sort(key=lambda i: i.hp)
		return True
	return False
def positionIn(fighters, p):
	for f in fighters:
		if p[0] == f.y and p[1] == f.x:
			return True

def printField(len):
	for y in range(len):
		for x in range(len):
			pos = [y, x]
			if pos in walls:
				print('#', end='')
			elif positionIn(elves, pos):
				print('E', end='')
			elif positionIn(goblins, pos):
				print('G', end='')
			else:
				print('.', end='')
		print()
	print()

main()