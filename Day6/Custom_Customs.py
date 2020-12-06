def replacer(initial_string, ch,  
         replacing_character, occurrence): 
      
    # breaking a string into it's 
    # every single character in list 
    lst1 = list(initial_string) 
    lst2 = list(ch) 
      
    # List to store the indexes in which 
    # it is replaced with the  
    # replacing_character 
    lst3 = [] 
      
    # Loop to find the Nth occurence of 
    # given characters in the string 
    for i in lst2: 
        if(lst1.count(i)>= occurrence): 
            count = 0
            for j in range(0, len(initial_string)): 
                if(i == lst1[j]): 
                    count+= 1
                    if(count >= occurrence): 
                        lst3.append(j) 
      
    for i in lst3: 
        # Replacing that particular index 
        # with the requested character  
        lst1[i] = replacing_character 
      
    # length of list with # removed      
    return len((''.join(lst1)).replace('#', ''))

def group_match(group_list):
    gcount = 0
    for groups in group_list:
        range(len(groups))
        for i in ch:
            match = True
            for j in range(len(groups)):
                if i in groups[j] and match == True:
                    match = True
                else:
                    match = False
            if match == True:
                gcount += 1

    return gcount
            
    
    
      
# Driver Code: 
if __name__ == '__main__': 

    file_location = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day6\custom_data.txt'
    data = [chunk.split() for chunk in open(file_location).read().split("\n\n")]
    ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    occurence = 2
    replacing_character = '#'
    data_append = []
    count = 0

    # join passengers into groups 
    for i in data:
        data_append.append(''.join(i))
    
    # for loop to check each group and pair out answers for same question more than one
    for i in data_append:
        count += replacer(i, ch, replacing_character, occurence) 
    
    print('Sum of all questions answered "YES": {0}'.format(count))

    gcount = group_match(data)

    print('Sum of all questions answered "YES" in a group: {0}'.format(gcount))

