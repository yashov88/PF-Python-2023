text = input()
result = text[0]

for ch in text:
    if ch == result[-1]:
        continue
    else:
        result += ch

print(result)