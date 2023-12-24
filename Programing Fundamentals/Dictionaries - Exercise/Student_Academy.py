grades_by_students = {}

n = int(input())

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in grades_by_students:
        grades_by_students[student_name] = []

    grades_by_students[student_name].append(student_grade)

for student,grades in grades_by_students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
