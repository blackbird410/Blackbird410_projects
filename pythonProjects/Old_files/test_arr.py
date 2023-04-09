array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
List = []
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] not in List:
            if array1[i] in array2[j]:
                List.append(array1[i])
                j = len(array2)
            else:
                continue
        else:
            continue
List.sort()
print(List)
