n = int(input())

start = 97

for first in range(start, start + n):
    for second in range(start, start + n):
        for third in range(start, start + n):
            print(chr(first), chr(second), chr(third), sep="")
