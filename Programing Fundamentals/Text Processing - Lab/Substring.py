word = input()
text = input()

while word in text:
    text = text.replace(word, "")

print(text)