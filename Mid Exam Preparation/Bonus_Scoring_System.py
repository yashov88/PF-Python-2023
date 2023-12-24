from math import ceil

students = int(input())
lecture = int(input())
bonus = int(input())

max_attendances = 0
for _ in range(students):
    attendances = int(input())
    max_attendances = max(attendances, max_attendances)

total_bonus = 0
if lecture != 0:
    total_bonus = (max_attendances / lecture) * (5 + bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
