words = input().split()

count_by_letter = {}

for word in words:
    for letter in word:
        if letter in count_by_letter:
            count_by_letter[letter] += 1
        else:
            count_by_letter[letter] = 1

for letter in count_by_letter:
    print(f"{letter} -> {count_by_letter[letter]}")
