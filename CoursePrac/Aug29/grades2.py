grades = []
names = ["John", "Michael", "Maria", "Jamal", "Thor"]
sum = 0
i = 0
for name in names:
    grade = int(input(f"Enter with the grade for {name} "))
    grades.append(grade)
    sum += grade
    i += 1

avg = sum / len(grades)
print("Average:_",avg)

max_grade = max(grades)
max_name = names[grades.index(max_grade)]
print(grades)
print(max_grade)
print(max_name)

