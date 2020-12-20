import re
from collections import deque

def final_math(parse_data):
    parse_data = parse_data.split()

    tv1 = tv2 = val = sign = None

    for char in parse_data:

        # if char != 'X':

            tv1, tv2, val, sign = evaluate_char(char, tv1, tv2, val, sign)

        # elif char == 'X':
        #     tv2 = paren_fields_math.popleft()
        #     tv1, tv2, val, sign = evaluate_char(char, tv1, tv2, val, sign)

    return val
    

def paren_math(paren_fields):
    # paren_fields = paren_fields[0].split()
    lst = deque()

    for grp in paren_fields:
        
        grp = grp.split()
        tv1 = tv2 = val = sign = None
    
        for char in grp:

            tv1, tv2, val, sign = evaluate_char(char, tv1, tv2, val, sign)

        lst.append(val)
        
    return lst



def evaluate_char(char, tv1, tv2, val, sign):

    if char == '+' or char == '*':
                sign = char

    elif char.isdigit() and tv1 == None:

        tv1 = int(char)

    elif (char.isdigit() and tv1):
        
        if char.isdigit():
            tv2 = int(char)

        if tv1 and tv2 and sign:

            if sign == '+':
                val = tv1 + tv2
                tv1 = val
                tv2 = sign = None

            elif sign == '*':
                val = tv1 * tv2
                tv1 = val
                tv2 = sign = None

    return tv1, tv2, val, sign

def sub_paren(data, pattern_RE, paren_fields_math):
    x = re.sub(pattern_RE, 'X', data)
    iter = range(len(paren_fields_math))

    for i in iter:
        x = x.replace('X', str(paren_fields_math.popleft()), 1)

    
    return x


def do_math(data):
    
    pattern_RE = re.compile(r'\(([^()]+)\)')

    paren_fields = [grp for grp in re.findall(pattern_RE, data)]
    parse_data = ''

    if paren_fields:
        paren_fields_math = paren_math(paren_fields)
        parse_data = sub_paren(data, pattern_RE, paren_fields_math)
  
    

        while re.findall(pattern_RE, parse_data):
            paren_fields = [grp for grp in re.findall(pattern_RE, parse_data)]
            paren_fields_math = paren_math(paren_fields)
            parse_data = sub_paren(parse_data, pattern_RE, paren_fields_math)

    if parse_data:
        answer = final_math(parse_data)
    else:
        answer = final_math(data)

    return answer

def loop_list(data):
    counter = 0

    for i in data:
    
        x = do_math(i)
        counter += x

    return counter
  
if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day18\input.txt'

    with open(input, 'r') as f:
        data = f.read().split('\n')
        # data = [i.replace(' ', '') for i in data]

    print('Sum Of Values: {0}'.format(loop_list(data)))