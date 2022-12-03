from string import ascii_letters
def chunks(lst, n):
    j = []
    for i in range(0, len(lst), n):
        j.append(lst[i:i + n])
    return j

j = 0

[(j := j + ascii_letters.index([i for i in batch[0] if i in batch[1] and i in batch[2]][0])+1) for batch in chunks(open("input").read().splitlines(), 3)]

print(j)