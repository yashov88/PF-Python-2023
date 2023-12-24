def is_valid_idx(index, seq):
    return 0 <= index <= len(seq)


text = input()

while True:
    line = input()
    if line == "End":
        break

    command_args = line.split(" ")
    command = command_args[0]

    if command == "Translate":
        old_char = command_args[1]
        new_char = command_args[2]

        text = text.replace(old_char, new_char)
        print(text)
    elif command == "Includes":
        substring = command_args[1]

        if substring in text:
            print("True")
        else:
            print("False")
    elif command == "Start":
        start_substring = command_args[1]
        if is_valid_idx(0, text):
            if start_substring in text[0:len(start_substring)]:
                print("True")
            else:
                print("False")
    elif command == "Lowercase":
        text = text.lower()
        print(text)
    elif command == "FindIndex":
        char_idx = command_args[1]
        if char_idx in text:
            print(text.rfind(char_idx))
    else:
        start_idx = int(command_args[1])
        count = int(command_args[2])

        if is_valid_idx(0, text):
            text = text[:start_idx] + text[count:]
            print(text)