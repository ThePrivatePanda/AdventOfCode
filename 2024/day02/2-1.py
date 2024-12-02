from itertools import combinations

def is_row_legal(nums: list[int]) -> bool:
    diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
    
    for diff in diffs:
        diff = abs(diff)
        if diff < 1 or diff > 3:
            return False
    
    is_increasing = all([diff > 0 for diff in diffs])
    is_decreasing = all([diff < 0 for diff in diffs])
    
    if not (is_increasing or is_decreasing):
        return False
    
    return True

def part_2(nums: list[int]) -> bool:
    for i in range(len(nums)-1):
        numscopy = nums.copy()
        numscopy.pop(i)
        if is_row_legal(numscopy):
            return True

    return False


inp = open("input.txt").readlines()

print(len([i for i in [part_2([int(k) for k in j.split(" ")]) for j in inp] if i]))
