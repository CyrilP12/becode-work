# Loops and iteration - Exercise 9
# Display students' names

all_students = [
    ["David", "Justine", "Valentin", "Axel", "Redouane"],
    ["Julie", "StÃ©phane", "Mostapha", "Claudiu", "Son"],
]


for students in all_students:
    for student in students:
        print(student, "is an alumni.")
