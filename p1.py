#!\bin\en pyth

# PART 1 
# ___________________________________________________________________________
class Circle:
    def __init__(self, radius):
        assert radius >=0, f"{radius} is incorrect as a radius value."

        self.radius = radius
    def area(self):
        return 3.14 * (self.radius**2)


print("\nTESTING PROGRAM 1\n---------------------------------\n")
#Short program 
#--------------

r = float(input("Please enter a circle radius : "))
c = Circle(r)
print(f"\nThe area of your circle is : {c.area()}")



# Part 2
# ___________________________________________________________________________
class Thing:
    def __init__(self, weight=0):
        assert weight >0, f"{weight} is not greater than zero."
        self.weight = weight

    def pound_to_kilo(self):
        """Convert an input in pound to kilograms."""
        return self.weight * 0.453592


print("\nTESTING PROGRAM 2\n---------------------------------\n")
w = float(input("\nEnter a pound weight : "))
t  = Thing(w)
print(f"Conversion : {w} pounds => {t.pound_to_kilo()} kilos") 


# Part 3
# __________________________________________________________________________

def celcius_to_fahr():
    try:
        data = float(input("Please enter the temperature in celcius : "))
        return (data * 9/5) + 32
    except:
        print("ERROR with your input.")

def fahr_to_celcius():
    try:
        data = float(input("Please enter the temperature in Fahr. : "))
        return (data - 32) * (5/9)
    except:
        print("ERROR with your input.")


# Main 
#------
print("\nTESTING PROGRAM 3\n---------------------------------\n")

n = 0
while n != 3:
    print("======================\n1) Celcius to Fahrenheit\n2) Fahrenheit to Celcius\n3)Quit\n")
    n = int(input("YOUR CHOICE : "))
    if n == 1:
        print(f"Your answer : {celcius_to_fahr()}\n")
    if n == 2:
        print(f"Your answer : {fahr_to_celcius()}\n")

        

