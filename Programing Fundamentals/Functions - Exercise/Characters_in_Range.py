def char_in_range(start, end):
    result = ""  # []
    for num in range(ord(start) + 1, ord(end)):
        result += f"{chr(num)} "  # result.append(char(num))

    return result


char_start = input()
char_end = input()
# result_chars = char_in_range(char_start, char_end)
print(char_in_range(char_start, char_end))
# print(" ", join(result_chars))
