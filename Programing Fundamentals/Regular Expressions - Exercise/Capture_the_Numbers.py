import re
pattern = r"\d+"

result = []
while True:
    line = input()
    if not line:
        break

    matches = re.findall(pattern, line)
    result.extend(matches)

print(" ".join(result))
