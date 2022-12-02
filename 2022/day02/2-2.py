# It's not great but it works and it's better than 42 IF statements.

win_map = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
}

print(sum([win_map[j][k] for j, k in [line.split(" ") for line in open("input").read().split("\n")]]))