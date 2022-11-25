#!\bin\env python

import random

def n_gen(n, s, e):
    for i in range(n):
        x = str(random.randint(s, e))
        print(f"\nPlease write this pinyin number : {x}\n")

    print("\nPROCESS FINISHED.")

n_gen(10, 1000, 100000000)

