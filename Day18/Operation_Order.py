""" 

--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?

 
"""
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

def sub_x(pattern_RE, data, ans):

    if re.search(pattern_RE, data) != None:

        x = re.sub(pattern_RE, 'X', data, 1)
        x = x.replace('X', str(ans))
    
    else:

        x = ans

    
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

def add(dataset):
    split_string = dataset.replace('(', '')
    split_string = split_string.replace(')', '')
    split_string = split_string.split()
    tv1 = tv2 = val = sign = None
    
    for char in split_string:

        tv1, tv2, val, sign = evaluate_char(char, tv1, tv2, val, sign)

    val = tv1

    return val
    


        


def do_adv_math(data):
    pattern_RE_paren = re.compile(r'\(([^()]+)\)')
    pattern_RE_add = re.compile(r'(\d+\s\+\s\d+)')
    pattern_RE_multiply = re.compile(r'(\d+\s\*\s\d+)')
      
    while not isinstance(data, int):

        data = re_check(data, pattern_RE_paren, pattern_RE_add, pattern_RE_multiply)
    
    return data

def re_check(data, pattern_RE_paren, pattern_RE_add, pattern_RE_multiply):

    while re.search(pattern_RE_add, data):
        match = re.search(pattern_RE_add, data)
        sum_ans = add(match.group(0))
        data = sub_x(pattern_RE_add, data, sum_ans)

    if re.search(pattern_RE_paren, data):
        match = re.search(pattern_RE_paren, data)
        sum_ans = add(match.group(0))
        data = sub_x(pattern_RE_paren, data, sum_ans)

    if re.search(pattern_RE_add, data) or re.search(pattern_RE_paren, data):
        pass
    elif re.search(pattern_RE_multiply, data):
        data = add(data)
    else:
        data = int(data)
        

    return data

    

def loop_list(data, advance = False):
    counter = 0

    for i in data:
        if advance == False:

            x = do_math(i)
            counter += x

        elif advance == True:

            x = do_adv_math(i)
            counter += x

    return counter

  
if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day18\input.txt'

    with open(input, 'r') as f:
        data = f.read().split('\n')
        # data = [i.replace(' ', '') for i in data]

    print('Sum Of Values: {0}'.format(loop_list(data, advance = True)))

