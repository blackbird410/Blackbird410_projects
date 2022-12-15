from budget import *

def test_create_spend_chart():
        food = Category("Food")
        entertainment = Category("Entertainment")
        business = Category("Business")
        food.deposit(900, "deposit")
        entertainment.deposit(900, "deposit")
        business.deposit(900, "deposit")
        food.withdraw(105.55)
        entertainment.withdraw(33.40)
        business.withdraw(10.99)
        actual = create_spend_chart([business, food, entertainment])
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        print("Actual : \n", actual, len(actual))
        print("Expected : \n", expected, len(expected))
        return actual == expected


print(test_create_spend_chart())