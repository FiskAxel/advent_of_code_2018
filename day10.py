import re
with open('input10.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	p = re.compile(r"position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d),  ?(-?\d)>")
	starsPos = []
	starsVel = []
	for i in input:
		s = p.findall(i)[0]
		starsPos.append([int(s[0]), int(s[1])])
		starsVel.append([int(s[2]), int(s[3])])		
	seconds = 0
	while True:
		seconds += 1
		for i in range(len(starsPos)):
			starsPos[i][0] += starsVel[i][0]
			starsPos[i][1] += starsVel[i][1]
		# Manually found where the text were forming by looking in wich direction the numbers where going
		# Probably doesn't work for most inputs.
		if starsPos[0][0] == 200:
			print("Part 1:")	
			for y in range(186, 200):
				for x in range(138, 206):
					if [x, y] in starsPos:
						print('#', end='')
					else:
						print('.', end='')
				print()
			print(f"Part 2: {seconds}")
			break
		# Runs in under 10 seconds