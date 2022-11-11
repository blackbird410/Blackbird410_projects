#!\bin\env python

def arithmetic_arranger(s):
    """This function takes a string as parameter and return an arranged string."""

    l = [x.split(" ") for x in s]
    for x in l:
        i = len(x[0])
        j = len(x[2])

        if i >= j:
            x[0] = "  " + x[0]
            x[2] = " " + (i-j) * " " + x[2]
        if i < j:
            x[0] = "  " + (j-i) * " " + x[0]
            x[2] = " " + x[2]
        x.append((max(i, j)+2) * "-")
    print(f"{l}\n\n")

    f_l = "    ".join(x[0] for x in l)
    s_l = "    ".join(x[1] + x[2] for x in l)
    l_l = "    ".join(x[3] for x in l)

    #f_l = [f"{x[0]}\n{x[1]}{x[2]}\n{x[3]}    " for x in l]
    print(f"{f_l}\n{s_l}\n{l_l}")


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
