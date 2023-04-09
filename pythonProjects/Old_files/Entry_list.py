import pandas as pd
import numpy as np

class Person:
    all = []
    def __init__(self, name, f_name, age, gender):
        assert age>= 0, f"The age entered is not greater or equal to zero."
        assert gender.upper() == "M" or "F", "Invalid gender."
        
        self.name = name
        self.f_name = f_name
        self.age = age
        self.gender = gender.upper()

        Person.all.append(self)

    def __repr__(self):
        return f"Person({self.name}, {self.f_name}, {self.age}, {self.gender})"
                


def entry(n):
    e = Person("", "", 0, "")
    ls = []
    for i in range(n):
        e.name = input('Enter the last name of person ' + str(i + 1) + ': ')
        e.f_name = input('Enter the first name of person ' + str(i + 1) + ': ')
        e.age = int(input('Enter the age of person ' + str(i + 1) + ': '))
        e.gender = input('Enter the gender of person ' + str(i + 1) + ': ')
        print('\n')

        ls.append(e)

    return ls


def decode(d_ls : []):
    ls_name = []
    ls_f_name = []
    ls_age = []
    ls_gender =[]
    
    nb = len(d_ls)

    for i in range(nb):
        ls_name.append(d_ls[i].name)
        ls_f_name.append(d_ls[i].f_name)
        ls_age.append(d_ls[i].age)
        ls_gender.append(d_ls[i].gender)

    ls_dict = {'Last name': ls_name, 'First name': ls_f_name, 'Age': ls_age, 'Gender': ls_gender}

    return pd.DataFrame(ls_dict)
    


num = int(input("Enter the number of person for data entry : "))

data_ls = entry(num)
df = decode(data_ls)
df.to_csv("Dataset.csv")

print("All list\n___________________\n", data_ls)
print("Dataframe list\n___________________\n", df)


  
