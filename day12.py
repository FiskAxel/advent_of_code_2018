with open('input12.txt', 'r') as puzzleInput:
	generations = ['...' + puzzleInput.readline()[15:].rstrip() + '...']
	puzzleInput.readline()
	input = puzzleInput.readlines()
	rules = {}
	for i in input:
		j = i.rsplit()
		rules[j[0]] = j[2]	
	for i in range(120):
		newGen = '...'
		for j in range(2, len(generations[i]) - 2):
			key = generations[i][j-2:j+3]
			newGen += rules[key]
		generations.append(newGen + '...')
	# "results" stores value of generation x in [0] and the diff from previous in [1].
	results = [[0, 0]]
	for g in generations:
		result = 0
		index = - 3 - 1 * generations.index(g)
		for p in g:
			if p == '#':
				result += 1 * index
			index += 1
		results.append([result, result - results[len(results) - 1][0]])
	results.pop(0)
	print(f"Part 1: {results[20][0]}")
	# I checked the first 300 generations and discovered that past nr112 the diff to next generation
	# was 87 for all of them. Then I tried if this was also true for the rest, wich it was. 
	print(f"Part 2: {results[112][0] + (50000000000 - 112) * 87}")