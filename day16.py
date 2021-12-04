def main():
	with open('input16.txt', 'r') as puzzleInput:
		c = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", 
			 "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr" ]
		codes = [c.copy() for _ in range(16)]
		input = puzzleInput.readlines()
		i = 0
		result = 0
		while True:
			if input[i][0] != 'B':
				break
			match = 0
			before = input[i][9:19].split(", ")
			before = [int(j) for j in before]
			ins = input[i + 1].rsplit()
			ins = [int(j) for j in ins]
			after = input[i + 2][9:19].split(", ")
			after = [int(j) for j in after]

			reg = before.copy()
			addr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "addr" in codes[ins[0]]:
				codes[ins[0]].remove("addr")
			
			reg = before.copy()
			addi(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "addi" in codes[ins[0]]:
				codes[ins[0]].remove("addi")
			
			reg = before.copy()
			mulr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			else:
				if "mulr" in codes[ins[0]]:
					codes[ins[0]].remove("mulr")
			
			reg = before.copy()
			muli(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "muli" in codes[ins[0]]:
				codes[ins[0]].remove("muli")
			
			reg = before.copy()
			banr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "banr" in codes[ins[0]]:
				codes[ins[0]].remove("banr")
			
			reg = before.copy()
			bani(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "bani" in codes[ins[0]]:
				codes[ins[0]].remove("bani")
			
			reg = before.copy()
			borr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "borr" in codes[ins[0]]:
				codes[ins[0]].remove("borr")
			
			reg = before.copy()
			bori(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "bori" in codes[ins[0]]:
				codes[ins[0]].remove("bori")
			
			reg = before.copy()
			setr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "setr" in codes[ins[0]]:
				codes[ins[0]].remove("setr")
			
			reg = before.copy()
			seti(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "seti" in codes[ins[0]]:
				codes[ins[0]].remove("seti")
			
			reg = before.copy()
			gtir(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "gtir" in codes[ins[0]]:
				codes[ins[0]].remove("gtir")
			
			reg = before.copy()
			gtri(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "gtri" in codes[ins[0]]:
				codes[ins[0]].remove("gtri")
			
			reg = before.copy()
			gtrr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "gtrr" in codes[ins[0]]:
				codes[ins[0]].remove("gtrr")
			
			reg = before.copy()
			eqir(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "eqir" in codes[ins[0]]:	
				codes[ins[0]].remove("eqir")
			
			reg = before.copy()
			eqri(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "eqri" in codes[ins[0]]:
				codes[ins[0]].remove("eqri")
			
			reg = before.copy()
			eqrr(reg, ins[1], ins[2], ins[3])
			if isEqual(reg, after):
				match += 1
			elif "eqrr" in codes[ins[0]]:
				codes[ins[0]].remove("eqrr")	
			
			if match >= 3:
				result += 1
			i += 4
		print(f"Part 1: {result}")

		r = []
		for _ in range(20):
			for a in codes:
				if len(a) == 1:
					if a[0] not in r:
						r.append(a[0])
					continue
				for b in a:
					if b in r:
						a.remove(b)

		reg = [0, 0, 0, 0]
		i += 2
		while i < len(input):
			ins = input[i].rsplit()
			ins = [int(j) for j in ins]
			if codes[ins[0]] == ["addr"]:
				addr(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["addi"]:
				addi(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["mulr"]:
				mulr(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["muli"]:
				muli(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["banr"]:
				banr(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["bani"]:
				bani(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["borr"]:
				borr(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["bori"]:
				bori(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["setr"]:
				setr(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["seti"]:
				seti(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["gtir"]:
				gtir(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["gtri"]:
				gtri(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["gtrr"]:
				gtrr(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["eqir"]:
				eqir(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["eqri"]:
				eqri(reg, ins[1], ins[2], ins[3])
			elif codes[ins[0]] == ["eqrr"]:
				eqrr(reg, ins[1], ins[2], ins[3])
			i += 1
		print(f"Part 2: {reg[0]}")
		
def isEqual(reg1, reg2):
	for i in range(len(reg1)):
		if reg1[i] != reg2[i]:
			return False
	return True
def addr(reg, a, b, c):
	reg[c] = reg[a] + reg[b]
def addi(reg, a, b, c):
	reg[c] = reg[a] + b
def mulr(reg, a, b, c):
	reg[c] = reg[a] * reg[b]
def muli(reg, a, b, c):
	reg[c] = reg[a] * b
def banr(reg, a, b, c):
	reg[c] = reg[a] & reg[b]
def bani(reg, a, b, c):
	reg[c] = reg[a] & b
def borr(reg, a, b, c):
	reg[c] = reg[a] | reg[b]
def bori(reg, a, b, c):
	reg[c] = reg[a] | b
def setr(reg, a, b, c):
	reg[c] = reg[a]
def seti(reg, a, b, c):
	reg[c] = a
def gtir(reg, a, b, c):
	if a > reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0
def gtri(reg, a, b, c):
	if reg[a] > b:
		reg[c] = 1
	else:
		reg[c] = 0
def gtrr(reg, a, b, c):
	if reg[a] > reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0
def eqir(reg, a, b, c):
	if a == reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0
def eqri(reg, a, b, c):
	if reg[a] == b:
		reg[c] = 1
	else:
		reg[c] = 0
def eqrr(reg, a, b, c):
	if reg[a] == reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0

main()