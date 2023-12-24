def odd_and_even_sum(digits_as_str):
    even_sum = 0
    odd_sum = 0

    for digit_as_str in digits_as_str:
        digit = int(digit_as_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"  # [even_sum, odd_sum]


num_as_str = input()
# result = odd_and_even(num_as_str)
print(odd_and_even_sum(num_as_str))
# print(f"Odd sum = {result[1]}, Even sum = {result[0]}")
