number = int(input())

for i in range(number):
    word = input()

    is_Pure = True

    for j in word:
        if j == "," or j == "." or j == "_":
            is_Pure = False
            break

    if is_Pure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
