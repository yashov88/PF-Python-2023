def smallest(numbers):  # number1, number2, number3
    # if number1 < number2 and number1 < number3:
    #     return number1
    # elif number2 < number1 and number2 < number3:
    #     return number2
    # else:
    #     return number3
    min_number = float("inf")
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest([num1, num2, num3]))
