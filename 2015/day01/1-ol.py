print(sum({'(': 1, ')': -1}.get(c, 0) for c in open("input.txt").read()))
print(next(i+1 for i, floor in enumerate(__import__('itertools').accumulate({'(':1,')':-1}[c] for c in open("input.txt").read())) if floor<0))
