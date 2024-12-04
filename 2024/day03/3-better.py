import re

pattern = re.compile(r"""
    mul\((?P<num1>\d{1,3}),\s*(?P<num2>\d{1,3})\)   |  # mul(a,b)
    (?P<do>do\(\))                                |  # do()
    (?P<dont>don't\(\))                             # don't()
""", re.VERBOSE)

total_sum_all = 0
total_sum_controlled = 0
multiplication_enabled = True

with open("input.txt") as file:
    for line_number, line in enumerate(file, start=1):
        for match in pattern.finditer(line):
            if match.group('dont'):  # don't()
                multiplication_enabled = False
            elif match.group('do'):  # do()
                multiplication_enabled = True
            elif match.group('num1') and match.group('num2'):  # mul(a,b)
                num1 = int(match.group('num1'))
                num2 = int(match.group('num2'))
                product = num1 * num2
                total_sum_all += product
                if multiplication_enabled:
                    total_sum_controlled += product


print("Total sum of all multiplications:", total_sum_all)
print("Total sum with control toggles:", total_sum_controlled)
