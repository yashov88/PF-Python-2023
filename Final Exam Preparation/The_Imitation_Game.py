decrypted_message = input()

data = input()

while data != "Decode":
    splitted_data = data.split("|")
    command = splitted_data[0]

    if command == "Move":
        n_letters = int(splitted_data[1])
        first_part = decrypted_message[:n_letters]
        second_part = decrypted_message[n_letters:]
        decrypted_message =  second_part + first_part
    elif command == "Insert":
        index = int(splitted_data[1])
        additional_str = splitted_data[2]

        decrypted_message = decrypted_message[:index] + additional_str + decrypted_message[index:]
    elif command == "ChangeAll":
        sub_string = splitted_data[1]
        replacement_str = splitted_data[2]

        decrypted_message = decrypted_message.replace(sub_string, replacement_str)

    data = input()

print(f"The decrypted message is: {decrypted_message}")