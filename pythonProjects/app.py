def sum_intervals(intervals):
    n_l = []
    x = []
    y = []
    s = 0
    i = 0
    j = len(intervals)
    intervals = sorted(intervals)
    if j == 0:
        return 0
    for elt in intervals:
        x.append(elt[0])
        y.append(elt[1])
    while i < j:
        k = 0
        v = False
        while k < j:
            if x[k] < y[i] < y[k]:
                if x[i] < x[k]:
                    n_l.append((x[i], y[k]))
                else:
                    n_l.append((x[k], y[k]))
                del x[i]
                del y[i]
                j -= 1
                v = True
            else:
                v = False
            k += 1
        if not v:
            ap = (x[i], y[i])
            if ap not in n_l:
                n_l.append(ap)
        i += 1
    for elt in n_l:
        s += (elt[1] - elt[0])
    return s


inter = [(-329, -42), (447, 456)]
print("SUM : " + str(sum_intervals(inter)))
