student1 = {"name": "Alice", "age": 18, "grade": [85, 84, 94]}
student2 = {"name": "Bob", "age": 19, "grade": [78, 82, 88]}
student3 = {"name": "Charlie", "age": 18, "grade": [92, 90, 95]}
students = [student1, student2, student3]
def calculateaveragegrade(student):
    total = sum(student["grade"])
    average = total / len(student["grade"])
    return average

for student in students:
    avg_grade = calculateaveragegrade(student)
    print(student["name"] + ", age" + str(student["age"]) + ". " + "Your average grade is " + str(avg_grade) + ".")
