def main():
	class worker:
		def __init__(self, timer, step):
			self.timer = timer
			self.step = step 
	with open('input07.txt', 'r') as puzzleInput:
		# Input parsing (doing abc2 = abc1.copy() didnt work)
		input = puzzleInput.readlines()
		abc1 = {}
		abc2 = {}
		for i in input:
			p = i.split()
			if p[7] not in abc1:
				abc1[p[7]] = [p[1]]
				abc2[p[7]] = [p[1]]
			else:
				abc1[p[7]].append(p[1])
				abc2[p[7]].append(p[1])
			if p[1] not in abc1:
				abc1[p[1]] = []
				abc2[p[1]] = []		

		# PART 1
		ready = []
		done = []
		while len(abc1) > 0:
			updateReady(ready, abc1)
			abc1.pop(ready[0])
			done.append(ready.pop(0))
			updateAbc(done, abc1)
		result = "".join(str(c) for c in done)
		print(f"Part 1: {result}")
		
		# PART 2
		done = []
		result = 0
		workers = []
		for _ in range(5):
			workers.append(worker(0, 0))
		workInProgress = False
		while len(abc2) > 0 or len(ready) > 0 or workInProgress:
			workInProgress = False
			updateReady(ready, abc2)
			deligateWork(workers, ready, abc2)
			for w in workers:
				w.timer -= 1
				if w.timer == 0:
					done.append(w.step)
					updateAbc(done, abc2)
					w.step = 0
				elif w.timer > 0:
					workInProgress = True
			result += 1
		print(f"Part 2: {result}")

def updateReady(ready, abc):
	for x in abc:
		if len(abc[x]) == 0 and x not in ready:
			ready.append(x)		
	ready.sort()
def updateAbc(done, abc):
	for x in abc:
		for c in abc[x]:
			if c in done:
				abc[x].remove(c)
def deligateWork(workers, ready, abc):
	for w in workers:
		if len(ready) > 0 and w.step == 0:
			abc.pop(ready[0])
			w.timer = ord(ready[0]) - 4
			w.step = ready.pop(0)	

main()