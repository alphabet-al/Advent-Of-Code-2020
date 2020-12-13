test = [1, 2, 3]
copy_of_test = test.copy()

test[0] = 15

print(test, copy_of_test)




def check_adjacency(y_coor, x_coor, adj_dict):
    adj_pointers = [( -1, -1 ), ( 0, -1 ), ( 1, -1 ), ( -1, 0 ), ( 1, 0 ), ( -1, 1 ), ( 0, 1 ), ( 1, 1 ) ]
    adj_counter = 0

    for i in adj_pointers:
        key_to_lookup = (y_coor + i[0], x_coor + i[1])
        if key_to_lookup in adj_dict:
            adj_counter += adj_dict[(y_coor + i[0], x_coor + i[1])]
        else:
            continue

    return adj_counter