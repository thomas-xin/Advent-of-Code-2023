session = "53616c7465645f5f323a6c5c332c87fbd52331d93a14c07469f5d276b013c7dcd5872ee4b40e1e93a9031e9980bd306baf5449575ab2bc5ec35f6d3d27acd085" # Insert your session ID here
get_text = lambda url: globals().setdefault("cache", {}).get(url) or (text := (urllib := __import__("urllib.request")).request.urlopen(urllib.request.Request(url, headers=dict(Cookie=f"session={session}"))).read().decode("utf-8")) and (globals()["cache"].__setitem__(url, text), text)[-1]


# 1-1
total = sum(int(digits[0]) * 10 + int(digits[-1]) for line in get_text("https://adventofcode.com/2023/day/1/input").splitlines() for digits in (__import__("re").findall(r"[0-9]", line),))
print("1-1 OL:", total)

# 1-2
total = sum(int(nummap.get(digits[0], digits[0])) * 10 + int(nummap.get(digits[-1], digits[-1])) for nummap in [{n: i for i, n in enumerate("zero one two three four five six seven eight nine".split())}] for line in get_text("https://adventofcode.com/2023/day/1/input").splitlines() for digits in (__import__("re").findall(r"(?=([0-9]|" + "|".join(nummap) + "))", line),))
print("1-2 OL:", total)

# 2-1
total = sum(num for bag in (dict(red=12, green=13, blue=14),) for game, cubeset in (line.split(": ", 1) for line in get_text("https://adventofcode.com/2023/day/2/input").splitlines()) for num in [int(game.removeprefix("Game "))] if not any((t := cubes.split()) and int(t[0]) > bag.get(t[1], 0) for cubes in cubeset.replace(";", ",").split(", ")))
print("2-1 OL:", total)

# 2-2
total = sum(__import__("functools").reduce(int.__mul__, bag) for cubeset in (line.split(": ", 1)[-1] for line in get_text("https://adventofcode.com/2023/day/2/input").splitlines()) for bag in [[max([int(n) for n, c in (t.split() for t in cubeset.replace(";", ",").split(", ")) if c == C] or (1,)) for C in "red green blue".split()]])
print("2-2 OL:", total)

# 3-1
total = sum(int(match.group()) for lines, nsym in [(get_text("https://adventofcode.com/2023/day/3/input").splitlines(), "0123456789.")] for y, line in enumerate(lines) for match in __import__("re").finditer(r"[0-9]+", line) for mx, Mx in match.regs if mx - 1 >= 0 and line[mx - 1] not in nsym or Mx < len(line) and line[Mx] not in nsym or any(y - 1 >= 0 and x >= 0 and x < len(lines[y - 1]) and lines[y - 1][x] not in nsym for x in range(mx - 1, Mx + 1)) or any(y + 1 >= 0 and x >= 0 and x < len(lines[y + 1]) and lines[y + 1][x] not in nsym for x in range(mx - 1, Mx + 1)))
print("3-1 OL:", total)

# 3-2
total = sum(a * b for a, b in (w for v in [(starmap.setdefault(y, {}).setdefault(mx - 1, []).append(num) if mx - 1 >= 0 and line[mx - 1] == "*" else starmap.setdefault(y, {}).setdefault(Mx, []).append(num) if Mx < len(line) and line[Mx] == "*" else None if y - 1 >= 0 and any(starmap.setdefault(y - 1, {}).setdefault(x, []).append(num) for x in range(mx - 1, Mx + 1) if x >= 0 and x < len(lines[y - 1]) and lines[y - 1][x] == "*") else None if y + 1 < len(lines) and any(starmap.setdefault(y + 1, {}).setdefault(x, []).append(num) for x in range(mx - 1, Mx + 1) if x >= 0 and x < len(lines[y + 1]) and lines[y + 1][x] == "*") else None) and False or starmap for lines, starmap in [(get_text("https://adventofcode.com/2023/day/3/input").splitlines(), {})] for y, line in enumerate(lines) for match in __import__("re").finditer(r"[0-9]+", line) for num in (int(match.group()),) for mx, Mx in match.regs][0].values() for w in v.values() if len(w) == 2))
print("3-2 OL:", total)

# 4-1
total = sum((wincount := len(win.intersection(curr))) and 2 ** (wincount - 1) for win, curr in ((set(map(int, w.split())), set(map(int, c.split()))) for line in get_text("https://adventofcode.com/2023/day/4/input").splitlines() for w, c in [line.split(": ", 1)[-1].split(" | ")]))
print("4-1 OL:", total)

# 4-2
total = sum([copies.__setitem__(i, copies[i] + winval) if i < len(copies) else copies.append(winval) for i in range(wincount)] and False or winval for copies in [[]] for line in get_text("https://adventofcode.com/2023/day/4/input").splitlines() for w, c in [line.split(": ", 1)[-1].split(" | ")] for winval, wincount in [(1 + (bool(copies) and copies.pop(0)), len(set(map(int, w.split())).intersection(map(int, c.split()))))])
print("4-2 OL:", total)