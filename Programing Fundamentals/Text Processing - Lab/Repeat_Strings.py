words = input().split()

result = [word * len(word) for word in words]
# for word in words:
#     result += word * len(word)

print(*result, sep="")
# print("".join(result))
