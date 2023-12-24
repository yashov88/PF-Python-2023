numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(numbers)):
    beggar_idx = idx % beggars_count
    num = int(numbers[idx])
    beggars[beggar_idx] += num

print(beggars)
