inp = open("input.txt").read()


# Part 1
curr_floor = 0
for char in inp:
    if char == "(":
        curr_floor += 1
    elif char == ")":
        curr_floor -= 1
    
print(curr_floor)


# Part 2
curr_floor = 0
for index, char in enumerate(inp):
    if char == "(":
        curr_floor += 1
    elif char == ")":
        curr_floor -= 1
    if curr_floor < 0:
        break

print(index+1)
