
while True:
    command_args = input().split()
    command = command_args[0]

    if command == "end":
        break

    chat = []

    if command == "Chat":
        message = command[1]
        chat.append(message)
    elif command == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)
        else:
            continue
    elif command == "Edit":
        message = command[1]
        new_message = command[2]

    elif command == "Pin":
        pass
    elif command == "Spam":
        pass

print(message)