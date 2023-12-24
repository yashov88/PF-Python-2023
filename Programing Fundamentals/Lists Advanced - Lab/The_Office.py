employees_happiness = [int(el) for el in input().split()]
improvement_factor = int(input())
employees_happiness = [el * improvement_factor for el in employees_happiness]

avg_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees_count = len([el for el in employees_happiness if el >= avg_happiness])
half_employees_count = len(employees_happiness) / 2

if happy_employees_count >= half_employees_count:
    print(f"Score: {happy_employees_count}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees_count}/{len(employees_happiness)}. Employees are not happy!")
