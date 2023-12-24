def min_num(numbers):
    min_number = float("inf")
    for num in numbers:
        if num < min_number:
            min_number = num
    return f"The minimum number is {min_number}"


def max_num(numbers):
    max_number = float("-inf")
    for num in numbers:
        if num > max_number:
            max_number = num
    return f"The maximum number is {max_number}"


def min_max_sum(numbers):
    sum_numbers = 0
    for digit_as_str in numbers:
        digit = int(digit_as_str)
        sum_numbers += digit
    return f"The sum number is: {sum_numbers}"


numbers_as_str = [int(x) for x in input().split()]
print(min_num(numbers_as_str))
print(max_num(numbers_as_str))
print(min_max_sum(numbers_as_str))
