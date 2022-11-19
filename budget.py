#!\bin\env python

import csv



class Category:
    ledger = []

    def __init__(self, name = ""):
        self.name = name

    def deposit(self, amount, description="", to=""):
        assert amount > 0, f"The amount {amount} is invalid."
        if to:
            Category.ledger.append({"name": to[0].upper()+to[1:],"amount": amount, "description": description})
        else:
            Category.ledger.append({"name": self.name,"amount": amount, "description": description})
    def withdraw(self, amount, description=""):
        assert amount >= 0, f"The amount {amount} is invalid."

        if not self.check_funds(amount):
            return False
        Category.ledger.append({"name": self.name,"amount": -amount, "description": description})
        return True

    def get_balance(self):
        l = Category.ledger

        if l == []:
            return 0
        else:
            bal = 0
            for x in l:
                if x['name'] != self.name:
                    continue
                bal += x.get("amount")
            return bal

    def transfer(self, amount, obj):

        b = self.check_funds(amount)
        if b :
            self.withdraw(amount, f"Transfer to {obj.name}")
            self.deposit(amount, f"Transfer from {self.name}", to=obj.name)
            return True
        return False

    def check_funds(self, amount):
        return amount < self.get_balance()

    def __repr__(self):
        l = Category.ledger
        l_amount = []
        rs = ""

        for x in l:
            if x['name'] != self.name:
                continue

            s = len(x['description'])
            a = str(format(x['amount'], '.2f'))
            a = (7-len(a)) * " " + a

            if s > 23:
                rs += x['description'][:23] + a
            else:
                rs += x['description'] + (23-s) * " " + a
            
            rs += "\n"
            l_amount.append(round(x['amount'],2))

        return f"{self.name.center(30, '*')}\n" + rs + f"Total: {sum(l_amount)}"



def create_spend_chart(l_cat:[]):
    rs = ""
    l = Category.ledger
    wd_per = []
    c = 0
    max_l = 1
    n_l = []

    for x in l_cat:
        if len(str(x.name)) > max_l:
            max_l = len(str(x.name))

    for cat in l_cat:
        s = 0
        for x in l:
            if x['name'].lower() == cat.name.lower():
                if x['amount'] < 0:
                    s += x['amount']
        tampon = list(cat.name) 
        n_l = [f" {y} " for y in tampon]
        
        c_bar = int(round(-s/120,1)*10 + 1)
        bar = ["   "] * (11 - c_bar) + c_bar * [" o "] + ['---'] + n_l + (max_l - len(x['name'])) * ["   "]
        wd_per.append(bar)

    bar_measures = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
    bar_measures += (max_l+1) * ["    "]

    for i in range(len(bar_measures)):
        rs += bar_measures[i]
        for j in range(len(l_cat)):
            rs += wd_per[j][i]
        rs += "\n"
    
    return "Percentage spent by category\n" + rs


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(f"**********BAR_CHART**********\n{create_spend_chart([food, clothing, auto])}")


