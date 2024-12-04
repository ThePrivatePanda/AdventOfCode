import re

inp = open("input.txt").read()

ans = 0

for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp):
    num1, num2 = map(int, match)  # Convert matched groups to integers
    ans += num1 * num2

print(ans)

ans = 0

multiplication_enabled = True
for match in re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|don't\(\)|do\(\)", inp):  # Use re.finditer for better control
    match_text = match.group(0)  # The full matched text
    if match_text == "don't()":
        multiplication_enabled = False
    elif match_text == "do()":
        multiplication_enabled = True
    else:
        num1, num2 = match.groups()
        if multiplication_enabled:
            product = int(num1) * int(num2)
            ans += product

print(ans)
