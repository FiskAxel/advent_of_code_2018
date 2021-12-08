doors = []
spaces = [[0, 0]]
thousandDoorsAway = 0

def main():
	with open('input20.txt', 'r') as puzzleInput:
		input = puzzleInput.readline()
		findDoors(0, 0, input)
		result = findPath(0, 0)
		print(f"Part 1: {result}")
		print(f"Part 2: {thousandDoorsAway}")
		#printMap()

def findDoors(y, x, c):
	# Splits string if '|' is not inside parenthesis
	open = 0
	for i, a in enumerate(c):
		if a == '|' and open == 0:
			path1 = c[:i]
			path2 = c[i + 1:]
			findDoors(y, x, path1)
			findDoors(y, x, path2)
			return
		elif a == '(':
			open += 1
		elif a == ')':
			open -= 1

	i = 0
	while i < len(c):
		if c[i] == 'N':
			doors.append([y - 1, x])
			spaces.append([y - 2, x])
			y -= 2
		elif c[i] == 'S':
			doors.append([y + 1, x])
			spaces.append([y + 2, x])
			y += 2
		elif c[i] == 'E':
			doors.append([y, x + 1])
			spaces.append([y, x + 2])
			x += 2
		elif c[i] == 'W':
			doors.append([y, x - 1])
			spaces.append([y, x - 2])
			x -= 2
		elif c[i] == '(':
			path = ""
			open = 0
			i += 1
			while c[i] != ')' or open > 0:
				if c[i] == '|' and '(' not in path:
					findDoors(y, x, path)
					path = ""
				else:
					path += c[i]
				if c[i] == '(':
					open += 1
				elif c[i] == ')':
					open -= 1
				i += 1
			findDoors(y, x, path)	
		i += 1
class queItem:
	def __init__(self, y, x, l):
		self.y = y
		self.x = x
		self.l = l
def findPath(y, x):
	"Breadh-first search"
	len = 0
	que = [queItem(0, 0, 0)]
	visited = []
	for q in que:
		y, x, l = q.y, q.x, q.l
		if [y - 1, x] in doors and [y - 1, x] not in visited:
			visited.append([y - 1, x])
			que.append(queItem(y - 2, x, l + 1))
		if [y + 1, x] in doors and [y + 1, x] not in visited:
			visited.append([y + 1, x])
			que.append(queItem(y + 2, x, l + 1))
		if [y, x + 1] in doors and [y, x + 1] not in visited:
			visited.append([y, x + 1])
			que.append(queItem(y, x + 2, l + 1))
		if [y, x - 1] in doors and [y, x - 1] not in visited:
			visited.append([y, x - 1])
			que.append(queItem(y, x - 2, l + 1))
		if len < l: 
			len = l
		if 1000 <= len: # For part 2
			global thousandDoorsAway
			thousandDoorsAway += 1
	return len
def printMap():
	minY, minX = float("inf"), float("inf")
	maxY, maxX = float("-inf"), float("-inf")
	for d in doors:
		if d[0] < minY:
			minY = d[0]
		if d[0] > maxY:
			maxY = d[0]
		if d[1] < minX:
			minX = d[1]
		if d[1] > maxX:
			maxX = d[1]
	for s in spaces:
		if s[0] < minY:
			minY = s[0]
		if s[0] > maxY:
			maxY = s[0]
		if s[1] < minX:
			minX = s[1]
		if s[1] > maxX:
			maxX = s[1]
	
	for y in range(minY - 1, maxY + 2):
		row = ""
		for x in range(minX - 1, maxX + 2):
			if y == 0 and x == 0:
				row += 'X'
			elif [y, x] in doors:
				row += '|'
			elif [y, x] in spaces:
				row += '.'
			else:
				row += '#'
		print(row)

main()