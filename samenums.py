def samenums(list1, list2):
    # 2 3 8 8 - sorted asc
    # 1 2 5 6 8 8 - sorted asc
    # return 2 8 8

    p1 = 0
    p2 = 0
    s = []

    while p1 < len(list1) and p2 < len(list2):

        if list1[p1] == list2[p2]:
            s.append(list1[p1])
            p1 += 1
            p2 += 1

        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1
    
    return s

print(samenums([2, 3, 8, 8], [1, 2, 5, 6, 8, 8]))
    

