#!\bin\env python

import csv



class Category:
    ledger = []

    def __init__(self, name = ""):
        self.name = name

    def deposit(self, amount, description=""):
        assert amount > 0, f"The amount {amount} is invalid."
        
        Category.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, decription=""):
        assert amount >= 0, f"The amount {amount} is invalid."

        if not self.check_funds():
            return False
        Category.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        l = Category.ledger

        if l == []:
            return 0
        else:
            bal = 0
            for x in l:
                bal += x.get("amount")
            return bal

    def transfer(self, amount, obj):
        b = self.withdraw(amount, f"Transfer to {obj.name}")
        if b :
            self.deposit(amount, f"Tranfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount < self.get_balance()



    @classmethod
    def instantiate_from_csv(cls, file_name):
        try:
            with open(file_name, "r") as f:
                reader = csv.DictReader(f)
                categories = list(reader)

            for category in categories:
                Category(
                        name = category.get("name")

                        )
        except:
            print("The file cannot be openned.")


    def __repr__(self):
        l = Person.ledger
        l_desc = []
        l_amount = []
        rs = ""

        for x in l:
            if x.name != self.name:
                continue
            s = len(x.description)
            if s > 23:
                rs += x.description[:23] + str(round(x.amount,2)) 
            else:
                rs += x.description + (23-s) * " " + str(round(x.amount,2))
            rs += "\n"
            l_amount.append(round(x.amount,2))
        rs += f"Total: {sum(l_amount)}"


        return f"{self.name.center(30, '*')}\n" + rs


