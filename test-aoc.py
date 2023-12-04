session = "53616c7465645f5f323a6c5c332c87fbd52331d93a14c07469f5d276b013c7dcd5872ee4b40e1e93a9031e9980bd306baf5449575ab2bc5ec35f6d3d27acd085" # Insert your session ID here

import requests
cache = {}
def get_text(url):
	try:
		return cache[url]
	except KeyError:
		with requests.get(url, cookies=dict(session=session)) as resp:
			resp.raise_for_status()
			cache[url] = resp.text
			return resp.text


# 1-1
import re
calibration = get_text("https://adventofcode.com/2023/day/1/input")
lines = calibration.splitlines()
total = 0
for line in lines:
	digits = re.findall(r"[0-9]", line)
	total += int(digits[0]) * 10 + int(digits[-1])
print("1-1:", total)

# 1-2
numnames = "zero one two three four five six seven eight nine".split()
nummap = {n: i for i, n in enumerate(numnames)}
total = 0
for line in lines:
	digits = re.findall(r"(?=([0-9]|" + "|".join(nummap) + "))", line)
	first, last = digits[0], digits[-1]
	total += int(nummap.get(first, first)) * 10 + int(nummap.get(last, last))
print("1-2:", total)


# 2-1
configuration = get_text("https://adventofcode.com/2023/day/2/input")
lines = configuration.splitlines()
bag = dict(
	red=12,
	green=13,
	blue=14,
)
total = 0
for line in lines:
	game, cubeset = line.split(": ", 1)
	num = int(game.removeprefix("Game "))
	exceeded = False
	for cubes in cubeset.replace(";", ",").split(", "):
		n, c = cubes.split()
		if int(n) > bag.get(c, 0):
			exceeded = True
			break
	if exceeded:
		continue
	total += num
print("2-1:", total)

# 2-2
import functools
total = 0
for line in lines:
	cubeset = line.split(": ", 1)[-1]
	bag = {}
	for cubes in cubeset.replace(";", ",").split(", "):
		n, c = cubes.split()
		n = int(n)
		if n > bag.get(c, 0):
			bag[c] = n
	total += functools.reduce(int.__mul__, bag.values())
print("2-2:", total)


# 3-1
schematic = get_text("https://adventofcode.com/2023/day/3/input")
lines = schematic.splitlines()
nsym = "0123456789."
total = 0
for y, line in enumerate(lines):
	for match in re.finditer(r"[0-9]+", line):
		mx = match.start() - 1
		Mx = match.end() + 1
		my = y - 1
		My = y + 1
		adjacent = False
		if mx >= 0 and line[mx] not in nsym:
			adjacent = True
		elif Mx - 1 < len(line) and line[Mx - 1] not in nsym:
			adjacent = True
		else:
			for x in range(mx, Mx):
				if my >= 0 and x >= 0 and x < len(lines[my]) and lines[my][x] not in nsym:
					adjacent = True
					break
				if My < len(lines) and x >= 0 and x < len(lines[My]) and lines[My][x] not in nsym:
					adjacent = True
					break
		if adjacent:
			total += int(match.group())
print("3-1:", total)

# 3-2
starmap = {}
for y, line in enumerate(lines):
	for match in re.finditer(r"[0-9]+", line):
		mx = match.start() - 1
		Mx = match.end() + 1
		my = y - 1
		My = y + 1
		num = int(match.group())
		if mx >= 0 and line[mx] == "*":
			starmap.setdefault(y, {}).setdefault(mx, []).append(num)
		elif Mx - 1 < len(line) and line[Mx - 1] == "*":
			starmap.setdefault(y, {}).setdefault(Mx - 1, []).append(num)
		else:
			for x in range(mx, Mx):
				if my >= 0 and x >= 0 and x < len(lines[my]) and lines[my][x] == "*":
					starmap.setdefault(my, {}).setdefault(x, []).append(num)
					break
				if My < len(lines) and x >= 0 and x < len(lines[My]) and lines[My][x] == "*":
					starmap.setdefault(My, {}).setdefault(x, []).append(num)
					break
total = 0
for v in starmap.values():
	for w in v.values():
		if len(w) == 2:
			a, b = w
			total += a * b
print("3-2:", total)

# 4-1
scratchcards = get_text("https://adventofcode.com/2023/day/4/input")
lines = scratchcards.splitlines()
total = 0
for line in lines:
	win, curr = line.split(": ", 1)[-1].split(" | ")
	win = set(map(int, win.split()))
	curr = set(map(int, curr.split()))
	winners = win.intersection(curr)
	if winners:
		total += 2 ** (len(winners) - 1)
print("4-1:", total)

# 4-2
scratchcards = get_text("https://adventofcode.com/2023/day/4/input")
lines = scratchcards.splitlines()
copies = []
total = 0
for line in lines:
	win, curr = line.split(": ", 1)[-1].split(" | ")
	win = set(map(int, win.split()))
	curr = set(map(int, curr.split()))
	winners = win.intersection(curr)
	wincount = len(winners)
	winval = 1
	if copies:
		winval += copies.pop(0)
	for i in range(wincount):
		try:
			copies[i] += winval
		except IndexError:
			copies.append(winval)
	total += winval
print("4-2:", total)