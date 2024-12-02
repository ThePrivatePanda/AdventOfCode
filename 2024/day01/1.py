print(sum(abs(a - b) for a, b in zip(*[sorted(nums) for nums in zip(*[(int(s) for s in line.strip().split()) for line in open("input.txt") if line.strip()])])))
print(sum(num * __import__('collections').Counter(int(line.split()[1]) for line in open('input.txt') if line.strip()).get(num, 0) for num in [int(line.split()[0]) for line in open('input.txt') if line.strip()]))
