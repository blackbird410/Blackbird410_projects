class Category:

    def __init__(self, name = ""):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        if description == "deposit" or description=="":
            self.ledger = []
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount

        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, obj):        
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {obj.name}")
            obj.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __repr__(self):
        l = self.ledger
        l_amount = []
        rs = ""

        for x in l:
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
    wd_per = []
    max_l = 1
    n_l = []
    m = 0
    init_depo = []

    a = []
    for x in l_cat:
        for y in x.ledger:
            a.append({"name": x.name, "amount": y["amount"], "description": y["description"]})

    exp_sum = 0
    for x in l_cat:
        for y in x.ledger:
            if y['amount'] < 0:
                exp_sum += y['amount']

        if len(str(x.name)) > max_l:
            max_l = len(str(x.name))

    for cat in l_cat:
        s = 0
        for x in a:
            if x['name'] == cat.name:
                if x['amount'] < 0:
                    s += x['amount']
                    if m < -x['amount']:
                        m = -x['amount']
        tampon = list(cat.name) 
        n_l = [f" {y} " for y in tampon]

        m = len(str(m))

        c_bar = int(round(s/exp_sum, 2)*10) + 1
        bar = ["   "] * (11 - c_bar) + c_bar * [" o "] + ['---'] + n_l + (max_l+1 - len(cat.name)) * ["   "]
        wd_per.append(bar)

    bar_measures = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
    bar_measures += (max_l+1) * ["    "]

    for i in range(len(bar_measures)):
        rs += bar_measures[i]
        for j in range(len(l_cat)):
            rs += wd_per[j][i]
        if rs[-1] == "-":
            rs += "-\n"
        else:
            rs += " \n"
    return "Percentage spent by category\n" + rs[:-2] + " "