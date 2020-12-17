def number_game(data, stop_value):
    sn_dict = dict((y,x) for x,y in enumerate(data, 1))
    multiple = {}
    spoken_number = data[len(data) - 1]
    # print(sn_dict)

    for turn in range(len(sn_dict) + 1, stop_value + 1):   
        
        if spoken_number in sn_dict and spoken_number not in multiple:
            spoken_number = 0
            
            if spoken_number in sn_dict:
                multiple[spoken_number] = sn_dict[spoken_number]

            sn_dict[spoken_number] = turn

        elif spoken_number in sn_dict and spoken_number in multiple:
             
            spoken_number = sn_dict[spoken_number] - multiple[spoken_number]

            if spoken_number in sn_dict:
                multiple[spoken_number] = sn_dict[spoken_number]

            sn_dict[spoken_number] = turn
            

    return spoken_number    



if __name__ == "__main__":
    data = [2,0,1,7,4,14,18]
    # data = [0,3,6]
    # data = [3,1,2]

    stop_value = 30000000

    print("Last Spoken Number: {0}".format(number_game(data, stop_value)))
