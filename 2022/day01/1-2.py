top = [sum([int(i) for i in elf_cal.split("\n")]) for elf_cal in [i for i in open("input").read().split("\n\n")]]
top.sort(reverse=True)

print(sum(top[:3]))