def arithmetic_arranger(s, b=False):
    """This function takes a string of mathematical operations and a boolean as parameters and return an arranged string. It returns the value of calculation if the boolean is set to True."""

  
    try:
      k = len(s)
      if k > 5:
        return 'Error: Too many problems.'

      r_l = ["", "", "", ""]
      
      for c in range(k):
        x = s[c].split(" ")
        i = len(x[0])
        j = len(x[2])

        # Checking errors
        if x[1] not in "+-":
          return "Error: Operator must be '+' or '-'."
        if not (x[0].isdigit() and x[2].isdigit()):
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

        # Appending spaces and numbers
        if c == 0:
          r_l[0] += x[0]
          r_l[1] += x[1] + x[2]
          r_l[2] += (max(i, j)+2) * "-"
          r_l[3] += " " * (max(i,j)-len(t) + 2) + t 
        else:
          r_l[0] += "    " + x[0]
          r_l[1] += "    " + x[1] + x[2]
          r_l[2] += "    " + (max(i, j)+2) * "-"
          r_l[3] += " " * (max(i,j)-len(t) + 6) + t

      if b:
        return "\n".join(r_l)
      else:
        return "\n".join(r_l[0:3])
        
    except:
      print("WRONG ENTRY, PLEASE TRY AGAIN WITH A CORRECT FORMAT.\n"
            "For example : arithmetic_arranger(['35 + 48', '478 -2585', '414 +21'])\n"
            "              arithmetic_arranger(['35 + 48', '478 -2585', '414 +21'], True)")