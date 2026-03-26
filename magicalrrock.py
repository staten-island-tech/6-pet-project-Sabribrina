def vendor (number, weight):
    total = 0
    my_list = 0
    for i in range (number):
        if weight[i] % 2:
            total += weight[i]
            my_list = total
            if my_list < total:
                my_list = total
        elif weight[i] % 2 != 0:
            total = 0
    print(my_list)
vendor(13, [2, 3, 4, 4, 5, 6, 1, 2, 2, 2, 1, 8, 2])