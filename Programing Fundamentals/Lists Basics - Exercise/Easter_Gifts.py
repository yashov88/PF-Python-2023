gifts = input().split()

while True:
    line = input()
    if line == "No Money":
        break

    command_agr = line.split()
    command = command_agr[0]
    gift = command_agr[1]

    if command == "OutOfStock":
        gift_idx = -1
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"
    elif command == "Required":
        idx = int(command_agr[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift
    elif command == "JustInCase":
        gifts[-1] = gift

for gift in gifts:
    if gift == "None":
        continue
    else:
        print(gift, end=" ")
