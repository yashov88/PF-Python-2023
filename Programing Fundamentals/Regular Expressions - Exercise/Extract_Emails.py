import re

pattern = r"\s(?P<User>[A-Za-z0-9][\w\-.]*[A-Za-z0-9])@(?P<Host>[A-Za-z][A-Za-z\-]+[A-Za-z]\.[A-Za-z][A-Za-z\.]*[A-Za-z])"

text = input()
matches = re.findall(pattern, text)

for match in matches:
    print(f"{match[0]}@{match[1]}")
