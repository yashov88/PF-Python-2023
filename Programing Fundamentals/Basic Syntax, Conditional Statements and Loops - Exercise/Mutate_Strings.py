first = input()
second = input()

result = first
for ind in range(len(first)):
    if first[ind] == second[ind]:
        continue

    result = second[:ind + 1] + first[ind + 1:]
    print(result)
