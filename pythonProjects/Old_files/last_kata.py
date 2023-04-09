def dirReduc(arr):
    di = []
    p = []
    i = 0
    k = len(arr)
    while i < k:
        if arr[i] == "NORTH" and arr[i+1] == "SOUTH":
            i += 2
        elif arr[i] == "EAST" and arr[i+1] == "WEST":
            i += 2
        else:
            di.append(arr[i])
            i += 1
    k = len(di)
    i = 0
    if k <= 1:
        return di
    while i < k-1:
        if di[i] == "SOUTH" and di[i+1] == "NORTH":
            i += 2
        elif di[i] == "WEST" and di[i+1] == "EAST":
            i += 2
        else:
            p.append(di[i])
            i += 1
    p.append(di[len(di) - 1])
    return p


a = ["NORTH", "SOUTH", "EAST", "WEST", "SOUTH", "NORTH", "WEST", "EAST"]
print(dirReduc(a))
