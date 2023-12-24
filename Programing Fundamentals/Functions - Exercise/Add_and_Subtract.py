# def add_and_subtract(first, second, third):
#     return first + second - third
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(add_and_subtract(num1, num2, num3))
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

sum_result = add(first, second)
result = subtract(sum_result, third)
print(result)
