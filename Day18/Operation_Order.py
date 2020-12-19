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

"""
from collections import deque

def reset_val(val, tv1, tv2, sign):
    tv1 = val
    sign = tv2 = None

    return tv1, tv2, sign

def do_math(data):
    total = 0   

    for line in data:
   
        mem = deque()
        mem_sign = deque()
        tv1 = None
        paren = 0
        val = None
        sign = None
        
        for char in line:

            if char == '(':

                if tv1:
                    mem.appendleft(tv1)                   
                if sign:
                    mem_sign.appendleft(sign)
                    tv1 = tv2 = sign = None


                paren += 1 

            elif char == ')':

                if tv1:
                    mem.appendleft(tv1)
                    tv1, tv2, sign = reset_val(val, tv1, tv2, sign)
                    tv1 = None
                
                paren -= 1

                if len(mem) > 1 and len(mem_sign) > 0:
                    sign = mem_sign.popleft()
                    tv2 = mem.popleft()
                    tv1 = mem.popleft()

                    if sign == '+':
                        val = tv1 + tv2
                        tv1 = val

                    elif sign == '*':
                        val = tv1 * tv2
                        tv1 = val
                
                if len(mem) != 0 and paren == 0:
                    tv1 = mem.popleft()
                 
                
            elif char == '+' or char == '*':
                sign = char


            elif char.isdigit() and tv1 == None:

                tv1 = int(char)

            elif char.isdigit() and tv1:

                tv2 = int(char)

                if tv1 and tv2 and sign:

                    if sign == '+':
                        val = tv1 + tv2
                        tv1, tv2, sign = reset_val(val, tv1, tv2, sign)

                    elif sign == '*':
                        val = tv1 * tv2
                        tv1, tv2, sign = reset_val(val, tv1, tv2, sign)

        
                    
        total += val
                        
                        
    return total            
            
if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day18\input.txt'

    with open(input, 'r') as f:
        data = f.read().split('\n')
        data = [i.replace(' ', '') for i in data]
    
    print('Sum Of Values: {0}'.format(do_math(data)))