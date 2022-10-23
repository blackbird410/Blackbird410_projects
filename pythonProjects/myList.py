class Person:

	all = []

	def __init__(self, last_name: str, first_name: str, age: int, gender: str,
                        weight: float, height: float,nationality: str, address: str, job: str):

		self.last_name = last_name
		self.first_name = first_name
		self.age = age
		self.gender = gender
		self.weight = weight
		self.height = height
		self.nationality = nationality
		self.address = address
		self.job = job

		Person.all.append(self)


my_list = []
n = 1

for i in range(n):
        print("Person " + str(i+1) + "\n_____________\n")
        name = input("Last name : ")
        f_name = input("First name : ")
        age = input("Age : ")
        gender = ""
        while (gender != "M" and gender != "F"):
                gender = input("Gender (M or F) : ")
        weight = input("Weight : ")
        height = input ("Height : ")
        nationality = input("Nationality : ")
        address = input("Address : ")
	job = input("Job : ")
	Person(name,f_name,age,gender,weight,height,nationality,address,job)

print(Person.all)