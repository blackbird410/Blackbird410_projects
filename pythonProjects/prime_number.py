# This program is to determine the prime numbers below a certain number.
# It will use the recursion method with a loop encrusted


def prime(n: int, prim: []):
    pr = [2, 3, 5, 7]
    if n <= 1:
        return 0
    else:
        ver = True
        for i in range(2, 10):
            if n not in pr and n % i == 0:
                print(n)
                ver = False
        if ver:
            prim.append(n)
        return prime(n-1, prim)


p = []
prime(int(input("NUMBER :")), p)
print(sorted(p))
print(sum(p))
