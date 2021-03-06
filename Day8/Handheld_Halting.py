'''
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu 
for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, 
but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) 
and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase 
the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the 
jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, 
and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other 
acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. 
It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a
 second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the 
corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing 
exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. 
If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. 
With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator 
after the program terminates?
'''
#############################################################################################################################################
import csv

def ac_acc(indx, acti, val, acc):
    acc += val
    indx += 1
    return indx, acc

def ac_jmp(indx, acti, val):
    indx += val
    return indx

def ac_nop(indx, acti, val):
    indx += 1
    return indx

def ins(lst):
    acc = 0
    current_index = 0
    traveled = []

    while current_index not in traveled and current_index >= 0 and \
            current_index not in traveled and current_index < len(lst):
        idx = lst[current_index][0]
        action = lst[current_index][1][0]
        value = int(lst[current_index][1][1])
        traveled.append(idx)

        if action == 'acc':
            current_index, acc = ac_acc(idx, action, value, acc)
        elif action == 'jmp':
            current_index = ac_jmp(idx, action, value)
        elif action == 'nop':
            current_index = ac_nop(idx, action, value)
    
    if current_index in traveled:
        # print('\nYou are stuck in a Loop!\n\nAccumulator value: {0}'.format(acc))
        return True, acc, traveled
    else:
        print('\nYou finished the game!\n\nAccumulator value: {0}'.format(acc))
        return False

def bad_jmp_nop(lst):
    ilist = jn_lst(lst)


    for i in ilist:
        
        if lst[i][1][0]  == 'jmp':
            lst[i][1][0] = 'nop'
        elif lst[i][1][0] == 'nop':
            lst[i][1][0]  = 'jmp'

        if not ins(lst):
            break
        else:
            if lst[i][1][0]  == 'jmp':
                lst[i][1][0] = 'nop'
            elif lst[i][1][0] == 'nop':
                lst[i][1][0]  = 'jmp'


def jn_lst(lst):
    lp, ac, trav_list = ins(lst)
    jmp_nop_list = []

    for i in trav_list:
        if lst[i][1][0] == 'jmp' or lst[i][1][0] == 'nop':
            jmp_nop_list.append(i)
    
    return jmp_nop_list



     

if __name__ == "__main__":

    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day8\move_data.txt'

    with open( input, 'r') as f:
        # mlist = list(enumerate(tuple(i.split()) for i in f.read().split('\n')))
        mlist = [row for row in enumerate(csv.reader(f, delimiter = ' '))]

    # loop, accumulator, trvlst = ins(mlist)
    # print('Infinite Loop Condition: {0}\tAccumulator Value: {1}'.format(loop, accumulator))
    
    bad_jmp_nop(mlist)
