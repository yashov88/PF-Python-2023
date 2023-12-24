resources = {}

while True:
    line = input()
    if line == "stop":
        break

    quantity = int(input())
    if line in resources:
        resources[line] += quantity
    else:
        resources[line] = quantity

for resources, quantity in resources.items():
    print(f"{resources} -> {quantity}")
