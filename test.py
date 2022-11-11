#!\bin\env python

def arithmetic_arranger(s):
    """This function takes a string as parameter and return an arranged string."""

    l = [x.split(" ") for x in s]
    f_l = [f"{x[0]}/n{x[1]} {x[2]}/n______" for x in l]
    for x in f_l:
        print(x)
    return l


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

