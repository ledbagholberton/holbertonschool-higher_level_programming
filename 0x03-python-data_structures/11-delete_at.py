def delete_at(my_list=[], idx=0):
    long = len(my_list)
    if idx < 0 or idx >= long:
        return my_list
    else:
        for i in range(idx, long - 1):
            my_list[i] = my_list[i + 1]
        del(my_list[long - 1])
    return my_list
