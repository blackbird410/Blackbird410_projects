#!\bin\env python

def arithmetic_arranger(s, b=False):
    """This function takes a string of mathematical operations and a boolean as parameters 
    and return an arranged string. It returns the value of calculation if the boolean is set to True."""

  
    try:
      if len(s) > 5:
        return 'Error: Too many problems.'

      l = [x.split(" ") for x in s]
      for x in l:
        i = len(x[0])
        j = len(x[2])

        # Checking errors
        if x[1] not in "+-":
          return "Error: Operator must be '+' or '-'."
        if not x[0].isdigit() or not x[2].isdigit():
          return "Error: Numbers must only contain digits."
        if i > 4 or j > 4:
          return "Error: Numbers cannot be more than four digits."

        if x[1] == "+":
          t = str(int(x[0]) + int(x[2]))
        else:
          t = str(int(x[0]) - int(x[2]))
                
        if i >= j:
          x[0] = "  " + x[0]
          x[2] = " " + (i-j) * " " + x[2]                
        if i < j:
          x[0] = "  " + (j-i) * " " + x[0]
          x[2] = " " + x[2]
            
        x.append((max(i, j)+2) * "-")
        x.append(" " * (max(i,j)-len(t) + 2) + t )   

      f_l = "    ".join(x[0] for x in l)
      s_l = "    ".join(x[1] + x[2] for x in l)
      l_l = "    ".join(x[3] for x in l)

      if b:
        c_l = "    ".join(x[4] for x in l)
        return f_l + "\n" + s_l + "\n" + l_l + "\n" + c_l
      else:
        return f_l + "\n" + s_l + "\n" + l_l 
    except:
      print("WRONG ENTRY, PLEASE TRY AGAIN WITH A CORRECT ONE.")


print(arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49']))
