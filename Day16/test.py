def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): 
            rt.extend(flatten(i))
        else: rt.append(i)
    return rt





if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day16\t_input.txt'

    with open(input, 'r') as f:
        # data_string = f.read().replace(' ', '_')
        # data = [i.split(':') for i in data_string.split('\n')]
        
        # data = [sub_lst.split() for lst in data for sub_lst in lst]
        # data = [sub_lst.split('') for lst in data for sub_lst in lst]

        # data = [re.findall(r'\d+[-]\d+', sub_lst) if re.findall(r'\d+[-]\d+', sub_lst) else sub_lst for lst in data for sub_lst in lst]

        # for i in range(data.count('')):
        #     data.remove('')
       
        # data = flatten(data)
        # data = [i.split('-') for i in data]
        # data = flatten(data)