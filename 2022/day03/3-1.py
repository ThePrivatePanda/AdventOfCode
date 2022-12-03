import string
j = 0
[((part1 := line[:len(line)//2], part2 := line[len(line)//2:]), j := j + 1 + string.ascii_letters.index([i for i in part1 if i in part2][0])) for line in open("input").read().splitlines()]

print(j)