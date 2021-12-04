def main():
	class cart:
		def __init__(s, x, y, dir):
			s.x = x
			s.y = y
			s.dir = dir #0U 1R 2D 3L
			s.m = 0 #0LeftTurn 1Forward 2RightTurn
		def forward(s):
			if s.dir == 0:
				s.y -= 1
			elif s.dir == 1:
				s.x += 1
			elif s.dir == 2:
				s.y += 1
			elif s.dir == 3:
				s.x -= 1
		def curveTurn(s, type):
			if type == '/':
				if s.dir == 0:
					s.dir = 1
				elif s.dir == 1:
					s.dir = 0
				elif s.dir == 2:
					s.dir = 3
				elif s.dir == 3:
					s.dir = 2
			elif type == '\\': 
				if s.dir == 0:
					s.dir = 3
				elif s.dir == 1:
					s.dir = 2
				elif s.dir == 2:
					s.dir = 1
				elif s.dir == 3:
					s.dir = 0
		def crossingTurn(s):
			s.dir = (s.dir + s.m - 1) % 4
			s.m = (s.m + 1) % 3		

	with open('input13.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		map = []
		carts = []
		for y in range(len(input)):
			map.append('')
			for x in range(len(input[y])):
				c = input[y][x]
				if c == '^' or c == 'v' or c == '>' or c == '<':
					if c == '^' or c == 'v':
						map[y] += '|'
						if c == '^':
							d = 0
						else: 
							d = 2
					elif c == '>' or c == '<':
						map[y] += '-'
						if c == '>':
							d = 1
						else:
							d = 3
					carts.append(cart(x, y, d))
				else:
					map[y] += input[y][x]
		part1 = [True]
		while len(carts) > 1:
			tick(carts, map, part1)
			carts.sort(key=lambda cart: cart.x)
			carts.sort(key=lambda cart: cart.y)
		print(f"Part 2: {carts[0].x},{carts[0].y}") # runs in a couple of seconds

def tick(carts, map, p1):
	remove = []
	for c in carts:
		c.forward()
		track = map[c.y][c.x]
		if track == '+':
			c.crossingTurn()
		elif track == '/':
			c.curveTurn(track)
		elif track == '\\':
			c.curveTurn(track)
		for d in carts:
			if c == d:
				continue
			if c.x == d.x and c.y == d.y:
				if p1[0]:
					print(f"Part 1: {c.x},{c.y}")
					p1[0] = False
				remove.append(c)
				remove.append(d)
				break
	for r in remove:
		carts.remove(r)

main()