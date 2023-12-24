import re

text = input()
matches = re.findall(r"([@#]+)([a-z]{3,})\W+/+(\d+)/+", text)

eggs = []

for match in matches:
    color = match[1]
    amount = int(match[2])

    eggs.append(f"You found {amount} {color} eggs!")

print("\n".join(eggs))
