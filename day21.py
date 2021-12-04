a, b, c, ip, d, e = 0, 0, 0, 0, 0, 0
seen = set()
while True:
	d = b | 65536
	b = 3798839
	while True:
		e = d & 255
		b += e
		b &= 16777215
		b *= 65899
		b &= 16777215
		if 256 > d:
			if len(seen) == 0:
				print(f"Part 1: {b}")
			if b in seen:
				print(f"Part 2: {prev}")
				exit()
			prev = b
			seen.add(b)
			break
		d = d // 256