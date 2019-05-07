def max_integer(my_list=[]):
    long = len(my_list)
    if long == 0:
        return None
    else:
        a = my_list[0]
        for i in range(1, long):
            if my_list[i] > a:
                a = my_list[i]
    return a
