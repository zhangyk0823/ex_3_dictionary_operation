student = {
    "name": "ZhangYukai",
    "student_id": "217230149",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


for key, value in student.items():
    print(f"{key}: {value}")


if "email" not in student:
    student["email"] = input("Enter an email: ")


new_city = input("Enter a new city: ")
while new_city.strip() == "":
    new_city = input("City cannot be empty. Enter a new city: ")
student["city"] = new_city


if student.get("phone") is None:
    print("Phone number not found.")


student["contact"] = {
    "phone": input("Enter a phone number: "),
    "email": student["email"]
}


student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}


total = 0
count = 0
for score in student["courses"].values():
    total += score
    count += 1
average_score = round(total / count, 1)


if average_score >= 90:
    student["academic_status"] = "Excellent"
elif average_score >= 75:
    student["academic_status"] = "Good"
elif average_score >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"


course_name = input("Enter a course name to search: ")
if course_name in student["courses"]:
    print(f"{course_name}: {student['courses'][course_name]}")
else:
    print("Course not found")


course_name = input("Enter the course name to update: ")
if course_name in student["courses"]:
    old_score = student["courses"][course_name]
    new_score = float(input("Enter the new score: "))
    while new_score < 0 or new_score > 100:
        new_score = float(input("Invalid score. Enter a number between 0 and 100: "))
    student["courses"][course_name] = new_score
    print(f"{course_name} score updated from {old_score} to {new_score}")
else:
    print("Course not found")


total = 0
count = 0
for score in student["courses"].values():
    total += score
    count += 1
average_score = round(total / count, 1)

if average_score >= 90:
    student["academic_status"] = "Excellent"
elif average_score >= 75:
    student["academic_status"] = "Good"
elif average_score >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"


print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print()
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print()
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print()
print("COURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score}")
print()
print(f"Average Score: {average_score}")
print(f"Academic Status: {student['academic_status']}")
print()
print("=====================================")
#（注：内容由AI生成）
