data = input()

guests = {}
unliked_meals = 0
while data != "Stop":
    splitted_data = data.split("-")
    command = splitted_data[0]
    guest = splitted_data[1]
    meal = splitted_data[2]

    if command == "Like":
        if guest not in guests:
            guests[guest] = {"meal": meal}
        else:
            guests[guest]["meal"] += meal
    else:
        unliked_meals += 1


    data = input()

print(guests)