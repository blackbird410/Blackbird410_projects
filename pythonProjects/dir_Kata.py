def dirReduc(arr):
    j = len(arr)
    i = 0
    while i < j:
        print(i)
        print(arr)
        if j - 1 > i >= 0:
            if arr[i] == "NORTH":
                if arr[i+1] == "SOUTH":
                    print((arr[i], arr[i + 1]))
                    del(arr[i])
                    del(arr[i])
                    print(arr)
                    j -= 2
                    i -= 2
            elif arr[i] == "SOUTH":
                if arr[i+1] == "NORTH":
                    print((arr[i], arr[i + 1]))
                    del (arr[i])
                    del (arr[i])
                    print(arr)
                    j -= 2
                    i -= 2
            elif arr[i] == "EAST":
                if arr[i + 1] == "WEST":
                    print((arr[i], arr[i + 1]))
                    del (arr[i])
                    del (arr[i])
                    print(arr)
                    j -= 2
                    i -= 2
            elif arr[i] == "WEST":
                if arr[i + 1] == "EAST":
                    print((arr[i], arr[i + 1]))
                    del (arr[i])
                    del (arr[i])
                    print(arr)
                    j -= 2
                    i -= 2
        i += 1

    return arr


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "SOUTH", "NORTH", "EAST"]
print("THIS : ", dirReduc(a))
