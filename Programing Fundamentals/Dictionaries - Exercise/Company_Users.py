employees_by_company = {}

while True:
    line = input()
    if line == "End":
        break

    args = line.split(" -> ")
    company_name = args[0]
    employee_id = args[1]

    if company_name not in employees_by_company:
        employees_by_company[company_name] = []

    if employee_id not in employees_by_company[company_name]:
        employees_by_company[company_name].append(employee_id)

for company, employees in employees_by_company.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
