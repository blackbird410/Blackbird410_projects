class Student:

    def __init__(self, lastname, firstname, age, major, gpa):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.major = major
        self.gpa = gpa


student = []
n = int(input("Number of student : "))

for i in range(n):
    student.append(Student(input("L_Name : "), input("F_Name : "), input("Age : "), input("Major : "), input("GPA : ")))

for x in student:
    print(str(x) + "\n")
