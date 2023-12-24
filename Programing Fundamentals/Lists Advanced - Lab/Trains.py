n_wagons = int(input())
train = [0] * n_wagons

# for i in range(n_wagons):
#     train.append(0)

commands = input()

while commands != "End":
    action = commands.split()[0]
    if action == "add":
        n_people = int(commands.split()[1])
        train[-1] += n_people
    elif action == "insert":
        index = int(commands.split()[1])
        n_people = int(commands.split()[2])
        train[index] += n_people
    elif action == "leave":
        index = int(commands.split()[1])
        n_people = int(commands.split()[2])
        train[index] -= n_people

    commands = input()

print(train)
