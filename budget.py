#!\bin\env python


class Category:
    ledger = []
    reg = []

    def __init__(self, name = ""):
        self.name = name

    def deposit(self, amount, description=""):

        Category.ledger.append({"amount": amount, "description": description})
        Category.reg.append(self.name)
        print(f"\n****Deposit of {amount} for {self.name}.\nTransactions : {Category.ledger}\n\n")


    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        Category.ledger.append({"amount": -amount, "description": description})
        Category.reg.append(self.name)

        return True

    def get_balance(self):
        l = Category.ledger
        r = Category.reg

        if l == []:
            return 0
        else:
            bal = 0
            for i in range(len(l)):
                if r[i] != self.name:
                    continue
                bal += l[i].get("amount")
            return bal

    def transfer(self, amount, obj):
        b = self.check_funds(amount)
        
        if b :
            self.withdraw(amount, f"Transfer to {obj.name}")
            obj.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __repr__(self):
        l = Category.ledger
        r = Category.reg
        l_amount = []
        rs = ""

        for i in range(len(l)):
            if r[i] != self.name:
                continue
            x = l[i]
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
    """This function creates a chart representing the expenses of each category."""

    rs = ""
    l = Category.ledger
    r = Category.reg
    wd_per = []
    max_l = 1
    n_l = []

    a = []
    for i in range(len(l)):
        a.append({"name": r[i], "amount": l[i]["amount"], "description": l[i]["description"]})

    for x in l_cat:
        if len(str(x.name)) > max_l:
            max_l = len(str(x.name))

    for cat in l_cat:
        s = 0
        for x in a:
            if x['name'] == cat.name:
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


#food = Category("Food")
#food.deposit(1000, "initial deposit")
#food.withdraw(10.15, "groceries")
#food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
#clothing = Category("Clothing")
#food.transfer(50, clothing)
#clothing.withdraw(25.55)
#clothing.withdraw(100)
#auto = Category("Auto")
#auto.deposit(1000, "initial deposit")
#auto.withdraw(15)

#print(f"**********BAR_CHART**********\n{create_spend_chart([food, clothing, auto])}")


