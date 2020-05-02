

    


def insert_val_at(index, my_list, value):
    # from end of my_list to index, move values up 1 index, then pass value in at the very end
    if index > len(my_list) - 1:
        return False
    rnge = len(my_list) - index
    last = len(my_list) - 1
    # create additional entry of final value
    my_list.append(my_list[last])
    i = last
    while i != index:
        print(i)
        my_list[i] = my_list[i - 1]
        i -= 1
    my_list[index] = value
    return my_list










