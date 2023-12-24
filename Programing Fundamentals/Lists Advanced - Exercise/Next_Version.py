major, minor, path = [int(x) for x in input().split(".")]

path += 1
if path == 10:
    path = 0
    minor += 1

    if minor == 10:
        minor = 0
        major += 1

print(f"{major}.{minor}.{path}")