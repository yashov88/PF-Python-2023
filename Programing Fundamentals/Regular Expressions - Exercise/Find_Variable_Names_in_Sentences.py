import re

pattern = r"\b_([A-Za-z\d]+)\b"

text = input()
matches = re.findall(pattern, text)

print(",".join(matches))
