import numpy as np
import re
with open('input03.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	part2 = []
	grid = np.zeros((1000, 1000))
	p = re.compile(r"(\d+),(\d+): (\d+)x(\d+)")
	for i in input:
		m = p.findall(i)[0]
		x, y, w, h = int(m[0]), int(m[1]), int(m[2]), int(m[3])
		grid[y:y+h,x:x+w] += np.ones((h,w))
		part2.append([x, y, w, h])
	result = np.count_nonzero(grid > 1)
	print(f"Part 1: {result}")

	for m in part2:
		x, y, w, h = m[0], m[1], m[2], m[3]
		if (grid[y:y+h,x:x+w] == np.ones((h,w))).all():
			result = part2.index(m) + 1
	print(f"Part 2: {result}")