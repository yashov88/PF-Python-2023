text = input()

encrypted_text = "".join(chr(ord(ch) + 3) for ch in text)

print(encrypted_text)
