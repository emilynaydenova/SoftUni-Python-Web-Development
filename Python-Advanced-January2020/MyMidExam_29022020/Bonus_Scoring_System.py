# Bonus Scoring System

import math

students_count = int(input())
lectures_count = int(input())
course_bonus = int(input())

students = {}  # bonus:attendances

if students_count > 0 and lectures_count > 0:
    for _ in range(students_count):
        attendances = int(input())
        if lectures_count > 0 and attendances > 0:
            students[attendances] = attendances / lectures_count * (5 + course_bonus)

    dd = max(students, key=students.get)  # !!!! max value in dictionary

    print(f'Max Bonus: {math.ceil(students[dd]):.0f}.')
    print(f'The student has attended {dd} lectures.')
else:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
