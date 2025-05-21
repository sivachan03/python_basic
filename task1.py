
student={'siva':22,'chan':22,'kiran':33}
name=input("Enter student name : ")
if name in student:
    print(f"{name} marks :{student[name]}")
else:
    print(f"No record found for student named {name}")
# print(student)