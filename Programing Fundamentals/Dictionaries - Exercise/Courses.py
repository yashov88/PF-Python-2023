students_by_course = {}

while True:
    line = input()
    if line == "end":
        break
    args = line.split(" : ")
    course_name = args[0]
    student_name = args[1]

    if course_name not in students_by_course:
        students_by_course[course_name] = []

    students_by_course[course_name].append(student_name)

for course_name, students in students_by_course.items():
    print(f"{course_name}: {len(students)}")

    for student in students:
        print(f"-- {student}")
