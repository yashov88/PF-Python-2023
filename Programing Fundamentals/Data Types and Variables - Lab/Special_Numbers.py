n = int(input())

# for num in range(1, n+1):
#     isSpecial = False
#     num_as_str = str(num)
#     sum_digit = 0
#     for char in num_as_str:
#         sum_digit += int(char)
#
#     if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
#         isSpecial = True
#
#     print(f"{num} -> {isSpecial}")
for num in range(1, n+1):
    isSpecial = False
    sum_digit = 0
    digit = num

    while digit:
        last_num = digit % 10
        sum_digit += last_num
        digit = digit // 10

    if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
        isSpecial = True
    print(f"{num} -> {isSpecial}")
