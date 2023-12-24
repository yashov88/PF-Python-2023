year = int(input())
year += 1
year_as_str = str(year)
while len(year_as_str) != len(set(year_as_str)):
    year += 1
    year_as_str = str(year)

print(year)
