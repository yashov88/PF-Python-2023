def calculate(command, first_num, second_num):
    result = 0
    if command == "multiply":
        result = first_num * second_num
    elif command == "divide":
        result = first_num // second_num
    elif command == "add":
        result = first_num + second_num
    elif command == "subtract":
        result = first_num - second_num

    return result


command_operator = input()
num1 = int(input())
num2 = int(input())

res = calculate(command_operator, num1, num2)
print(res)
