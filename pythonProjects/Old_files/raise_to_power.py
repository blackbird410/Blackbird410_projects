def r_to_p(base, p):
    if p == 1:
        print("RECURSION BOTTOM")
        return base
    elif p < 0:
        return 1/base
    else:
        c = r_to_p(base, p-1)
        print("{} * {}".format(base, c))
        return base * c


x = input("NUMBER : ")
y = input("Power : ")
print("RESULT : ", r_to_p(int(x), int(y)))
