input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day4\passport_data.txt'

pass_list = []
p_dict = {}
check = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

with open( input, 'r' ) as f:
    data = f.read().splitlines()
    x = ' '.join(data)
    x = x.split('  ')
    

for i in x:
    idx = dict((x.strip(), y.strip()) 
             for x, y in (element.split(':')  
             for element in i.split())) 
    pass_list.append(idx)

# for loop to check if valid keys are in each passenger

count = 0
for i in pass_list:
    if all(k in i for k in check):
        if int(i.get('byr')) >= 1920 and int(i.get('byr')) <= 2002:
            if int(i.get('iyr')) >= 2010 and int(i.get('iyr')) <= 2020:
                if int(i.get('eyr')) >= 2020 and int(i.get('eyr')) <= 2030:
                    if ('cm' in i.get('hgt') and int(i.get('hgt')[:-2]) >= 150 and int(i.get('hgt')[:-2]) <= 193) or \
                    ('in' in i.get('hgt') and int(i.get('hgt')[:-2]) >= 59 and int(i.get('hgt')[:-2]) <= 76):
                        if i.get('hcl')
                        
                        
                        
                        
                        count += 1
    
print(count)
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''