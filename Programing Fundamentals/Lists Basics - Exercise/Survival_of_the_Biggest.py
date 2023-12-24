numbers = [int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    min_number = min(numbers)
    numbers.remove(min_number)

print(", ".join([str(x) for x in numbers]))
