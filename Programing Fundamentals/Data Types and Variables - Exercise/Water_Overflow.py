water = 255
n = int(input())
capacity = 0

for _ in range(n):
    pour = int(input())

    if capacity + pour > water:
        print("Insufficient capacity!")
    else:
        capacity += pour

print(capacity)
