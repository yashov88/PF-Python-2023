dungeons_rooms = input().split("|")

max_health = 100
health = max_health
bitcoins = 0
room_count = 0

for rooms in dungeons_rooms:
    room_count += 1
    command, amount = rooms.split()
    # Try with floats if errors
    amount = int(amount)

    if command == "potion":
        if health + amount > max_health:
            print(f"You healed for {max_health - health} hp.")
            health = max_health
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            exit()

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
