travel_route = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())


for route in travel_route:
    command_args = route.split()
    command = command_args[0]

    if starting_fuel < 0:
        print("Mission failed.")
        break

    if command == "Travel":
        amount = command_args[1]
        amount = int(amount)
        distance = amount
        starting_fuel -= distance
        if starting_fuel > amount:
            print(f"The spaceship travelled {distance} light-years.")
    elif command == "Enemy":
        amount = command_args[1]
        amount = int(amount)
        enemy_armor = amount
        if starting_ammunition >= enemy_armor:
            starting_ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            run_fuel = (starting_ammunition - enemy_armor) * 2
            starting_fuel += run_fuel
            if starting_fuel < 0:
                continue
            else:
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
    elif command == "Repair":
        amount = command_args[1]
        amount = int(amount)
        resources = amount
        starting_fuel += resources
        starting_ammunition += resources * 2
        print(f"Ammunitions added: {(resources * 2)}.")
        print(f"Fuel added: {resources}.")

    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        exit(0)
