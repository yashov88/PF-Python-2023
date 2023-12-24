import re
text = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

#results = re.match(pattern, text)
results = re.findall(pattern, text)

#print(" ".join(results))
print(*results)