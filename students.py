student1 = {"name": "Alice", "grade": [79,54,90,79,94]}
student2 = {"name": "Bob", "grade": [88,92,85,90,91]}
student3 = {"name": "Charlie", "grade": [95,90,92,88,94]}
student4 = {"name": "David", "grade": [85,88,90,87,89]}
student5 = {"name": "Eve", "grade": [92,94,91,93,95]}
students = [student1, student2, student3,student4,student5]
def calcavggrade(student):
    total = sum(student["grade"])
    average = total / len(student["grade"])
    return average
def addtodict(student):
    avg=calcavggrade(student)
    student["average"]= avg
def gradelvl(student):
    if student["average"] >= 90:
            student["gradelevel"] = "A"
    elif student["average"] >= 80:
            student["gradelevel"] = "B"  
    elif student["average"] >= 70:
            student["gradelevel"] = "C"
    elif student["average"] >= 60:
            student["gradelevel"] = "D"

topgrade = ["name", 0]

for student in students:
    addtodict(student)
    gradelvl(student)
    print(f"{student['name']} , Your average grade is {student['average']} and your grade level is {student['gradelevel']} .")
    if student["average"] > topgrade[1]:
          topgrade[0] = student["name"]
          topgrade[1] = student["average"]

print(f"The student with the highest average grade is {topgrade[0]} with an average of {topgrade[1]}.")


    

