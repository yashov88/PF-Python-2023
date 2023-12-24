numbers = [int(x) for x in input().split(", ")]

positive_nums = [x for x in numbers if x >= 0]
negative_nums = [x for x in numbers if x < 0]
even_nums = [x for x in numbers if x % 2 == 0]
odd_nums = [x for x in numbers if x % 2 != 0]

print(f"Positive: {', '.join([str(x) for x in positive_nums])}")
print(f"Negative: {', '.join([str(x) for x in negative_nums])}")
print(f"Even: {', '.join([str(x) for x in even_nums])}")
print(f"Odd: {', '.join([str(x) for x in odd_nums])}")
