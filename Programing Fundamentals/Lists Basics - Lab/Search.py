n = int(input())

word = input()
all_str = []
str_containing_word = []

for _ in range(n):
    current_str = input()
    all_str.append(current_str)

    if word in current_str:
        str_containing_word.append(current_str)

print(all_str)
print(str_containing_word)
