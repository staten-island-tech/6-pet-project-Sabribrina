def vendor (number, weight):
    total = 0
    my_list = []
    for i in range (number):
        if i % 2:
            total += i
            my_list.append(total)
        else:
            total = 0
    print(my_list)
    print(max(my_list))

vendor(13, [2, 3, 4, 4, 5, 6, 1, 2, 2, 2, 1, 8, 2])