input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day13\t_input.txt'


data = open(input, 'r').read().split('\n')
data = data[1].split(',')
# data = ['17','x','13','19']
B = [(int(data[k]), k) for k in range(len(data)) if data[k] != 'x']

lcm = 1
time = 0    
for i in range(len(B)-1):
	bus_id = B[i+1][0]
	idx = B[i+1][1]
	lcm *= B[i][0]
	while (time + idx) % bus_id != 0:
		time += lcm
print(time)


'''
def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, red_adv, green_len, grn_adv):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, red_adv % red_len, green_len, grn_adv % green_len
    )
    # return -phase % period
    return period, phase


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


print(arrow_alignment(red_len=17, red_adv=0, green_len=13, grn_adv=2))
print(arrow_alignment(red_len=221, red_adv=119, green_len=19, grn_adv=3))
'''
