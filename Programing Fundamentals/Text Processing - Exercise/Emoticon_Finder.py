text = input()

for idx in range(len(text)):
    ch = text[idx]
    if ch == ":" and idx + 1 < len(text):
        symbol = text[idx + 1]
        print(f":{symbol}")
