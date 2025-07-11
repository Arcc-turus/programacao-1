def i_l(a = [], b = []):
    l = []
    e = True
    for i in range(6):
        if e:
            if i == 0:
                l.append(a[i])
            if i == 2:
                l.append(a[1])
            if i == 4:
                l.append(a[2])
            e = False
        elif not e:
            if i == 1:
                l.append(b[0])
            if i == 3:
                l.append(b[1])
            if i == 5:
                l.append(b[2])
            e = True
    return l

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]

print(i_l(l1, l2))