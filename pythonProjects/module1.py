# Linear_Search_Algo

def Linear_search(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return None


def verify(index):
    if index is None:
        print('Target is not found in list.')
    else:
        print('Target found at index : ', index)


myList = [47, 66, 27, 81, 4, 52]
verify(Linear_search(myList, int(input('Which number do you want to locate in the list ?\n'))))
