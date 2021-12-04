import numpy as np
import re
with open('input04.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	input.sort()
	pID = re.compile(r"#(\d+)")
	pTime = re.compile(r":(\d{2})")
	# Gets list of sleepingtimes for all guards
	guards = {}
	for i in input:
		if '#' in i:
			id = pID.findall(i)[0]
			if id not in guards:
				guards[id] = []
		elif 'falls asleep' in i:
			sTime = pTime.findall(i)[0]
		elif 'wakes up' in i:
			wTime = pTime.findall(i)[0]
			guards[id].append([int(sTime), int(wTime)])
	# Finds sleepiest guard
	max = 0
	for g in guards:
		tot = 0
		for s in guards[g]:
			tot += s[1] - s[0]
		if tot > max:
			max = tot
			sleepiestGuard = g
	# Finds sleepiest guard's sleepiest minute
	mins = np.zeros(60, dtype=np.int16)
	for s in guards[sleepiestGuard]:
		mins[s[0]:s[1]] += 1
	sleepiestMinute = np.where(mins == np.max(mins))[0][0]

	result = sleepiestMinute * int(sleepiestGuard)
	print(f"Part 1: {result}")

	# PART 2

	max = 0
	for g in guards:
		mins = np.zeros(60, dtype=np.int16)
		for s in guards[g]:
			mins[s[0]:s[1]] += 1
		if np.max(mins) > max:
			max = np.max(mins)
			theRealSleepiestMinute = np.where(mins == np.amax(mins))[0][0]
			guard2 = int(g)
	result = guard2 * theRealSleepiestMinute
	print(f"Part 2: {result}")