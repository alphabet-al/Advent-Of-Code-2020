""" 
--- Day 14: Docking Data ---
As your ferry approaches the sea port, the captain asks for your help again. The computer system that runs this port isn't compatible with the docking program on the ferry, 
so the docking parameters aren't being correctly initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses a strange bitmask system in its initialization program. Although you don't have the correct 
decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers. 
For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit)
 on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves 
 the bit in the value unchanged.

For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
This program starts by specifying a bitmask (mask = ....). The mask it specifies will overwrite two bits in every written value: the 2s bit is overwritten with 0, and the 64s
 bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)
So, because of the mask, the value 73 is written to memory address 8 instead. Then, the program tries to write 101 to address 7:

value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)
This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. Finally, the program tries to write 0 to address 8:

value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)
64 is written to address 8 instead, overwriting the value that was there previously.

To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. (The entire 36-bit address space 
begins initialized to the value 0 at every address.) In the above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a sum of 165.

Execute the initialization program. What is the sum of all values left in memory after it completes? 

--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
"""
import re 
from collections import deque
import itertools

def docking_prog_v2(data):
    mem_dict = {}

    for list_length in range(len(data)):
        key_val, data_val = get_val(data)

        if 'mask' in key_val:
            mask = store_mask(key_val, data_val)

        elif 'mem' in key_val:
            key_val, bin_memory = store_bin_key(key_val, data_val)
            result, float_count = eval_bitmask_v2(mask, bin_memory)
            mem_dict = all_pos_val(result, float_count, data_val, mem_dict)

    return sum(mem_dict.values())        

def docking_prog(data):
    mem_dict = {}

    for list_length in range(len(data)):
        key_val, data_val = get_val(data)

        if 'mask' in key_val:
            mask = store_mask(key_val, data_val)

        elif 'mem' in key_val:
            key_val, bin_val = store_kbit(key_val, data_val)
            result = eval_bitmask(mask, bin_val, key_val)
            mem_dict[key_val] = result
        
    
    return sum(mem_dict.values())
   
def get_val(data):
    val = data.popleft()
    for k,v in val.items():
        key_val = k
        data_val = v

    return key_val, data_val

def store_mask(key_val, data_val):
    if 'mask' in key_val:
        mask = data_val
        return mask

def store_kbit(key_val, data_val):

    bin_val = format(int(data_val), '036b')

    return key_val, bin_val

def store_bin_key(key_val, data_val):
    mem_num = (re.findall(r'\d+', key_val))
    bin_memory = format(int(mem_num[0]), '036b')

    return key_val, bin_memory

def eval_bitmask(mask, bin_val, key_val):
    result = deque()

    for bit in reversed(range(len(mask))):

        if (mask[bit] == 'X' and bin_val[bit] == '1') or (mask[bit] == 'X' and bin_val[bit] == '0'):
            result.appendleft(bin_val[bit])

        elif mask[bit] == '1' or '0':
            result.appendleft(mask[bit])

    return int(''.join(result),2)

def eval_bitmask_v2(mask, bin_memory):
    result = []
    float_count = 0

    for bit in reversed(range(len(mask))):

        if mask[bit] == 'X':
            result.append(mask[bit])
            float_count += 1
        
        elif mask[bit] == '0':
            result.append(bin_memory[bit])
        
        elif mask[bit] == '1':
            result.append(mask[bit])
        
    result.reverse()

    return result, float_count

def all_pos_val(result, float_count, data_val, mem_dict):

    permutation_deque = deque()
    lst = list(itertools.product([0, 1], repeat=float_count))
    old_result = result.copy()
    permutation_list = []
    
    for i in lst:
        for j in i:
            permutation_deque.append(j)


    for i in range(len(lst)):
        result = old_result.copy()
        for i_val in reversed(range(len(result))):
            if result[i_val] == 'X':
                result[i_val] = str(permutation_deque.popleft())

        permutation_list.append(result)
    
    for i in permutation_list:
        mem_dict[int(''.join(i),2)] = int(data_val)

    return mem_dict
       
                 




if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day14\input.txt'

    with open(input, 'r') as f:
        data = f.read().split('\n')
        data_list = [dict([i.split(' = ')]) for i in data]
        queue = deque()

        for i in data_list:
            queue.append(i)

        
    # print('Sum of all values left in memory: {0}'.format(docking_prog(queue)))
    print('Sum of all values left in memory: {0}'.format(docking_prog_v2(queue)))
   