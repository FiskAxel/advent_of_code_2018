depth = 5913
tX, tY = 8, 701
# depth = 510
# tX, tY = 10, 10
cave = {} # 0:erosion 1:type
def main():
	for y in range(tY + 100):
		for x in range(tX + 100):
			erosion(x, y)
	for y in range(tY + 100): 
		for x in range(tX + 100):
			type(x, y)
	print(f"Part 1: {riskLevel()}")
	print(f"Part 2: {aStarSearch()}") # Is SUPER SLOW but gave me the right output... :'(

def erosion(x, y):
	k = key(x, y)
	if k in cave:
		return cave[k][0]
	if (y == 0 and x == 0) or (y == tY and x == tX):
		cave[k] = 0
	elif y == 0:
		cave[k] = x * 16807
	elif x == 0:
		cave[k] = y * 48271
	else:
		up, left = key(x, y - 1), key(x - 1, y)
		cave[k] = cave[up] * cave[left]
	cave[k] += depth
	cave[k] %= 20183		
def type(x, y):
	k = key(x, y)
	cave[k] %= 3
def riskLevel():
	riskLevel = 0
	for y in range(tY + 1):
		for x in range(tX + 1):
			riskLevel += cave[key(x, y)]
	return riskLevel

def key(x, y):
	return str(x) + ',' + str(y)
def toKey(x, y, tool):
	return str(x) + ',' + str(y) + ',' + str(tool)
def h(x, y, tool):
	toolCost = 0
	if tool != 1:
		toolCost = 7 # Since you need to switch to torch at the target.
	return abs(tY - y) + abs(tX - x) + toolCost
class queItem:
	def __init__(self, x, y, tool, cost, estCost):
		self.x = x
		self.y = y
		self.tool = tool # 0:neither 1:torch 2:climbingGear. This means tool is not aloud if it equals the regions type (0 rocky, 1 wet, 2 narrow).
		self.cost = cost # From entrance
		self.estCost = estCost # Lowest estimated cost from here to target (result of heuristic function)
bestVisits = {}
que = [queItem(0, 0, 1, 0, h(0, 0, 1))]
def aStarSearch():
	while True:
		q = que[0]
		x, y, tool, cost = q.x, q.y, q.tool, q.cost
		key = toKey(x, y, tool)
		if key in bestVisits and bestVisits[key] <= cost:
			que.remove(q)
			continue
		bestVisits[key] = cost
		if x == tX and y == tY:
			if tool != 1:
				cost += 7
			return cost
		for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
			visit(x + dx, y + dy, tool, cost, x, y)		
		que.remove(q)
		que.sort(key=lambda i: i.cost + i.estCost)
def visit(x, y, tool, cost, px, py):
	if x < 0 or y < 0 or 50 < x or 750 < y:
		return
	cost += 1
	if cave[key(x, y)] != tool:
		que.append(queItem(x, y, tool, cost, h(x, y, tool)))
	cost += 7
	for _ in range(2):
		tool = (tool + 1) % 3
		if cave[key(px, py)] != tool and cave[key(x, y)] != tool:
			que.append(queItem(x, y, tool, cost, h(x, y, tool)))

main()