def student_id(name, roll, dept):
    print(f"{name} | Roll: {roll} | Dept: {dept}")

for i in range(2):
    name, roll, dept = input().split()
    student_id(name, roll, dept)