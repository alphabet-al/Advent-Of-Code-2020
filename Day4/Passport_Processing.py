import re

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day4\passport_data.txt'

pass_list = []
p_dict = {}
check = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
r = re.compile('#[0-9a-f]{6}')
ecl_type = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

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
                        if len(i.get('hcl')) == 7 and r.match(i.get('hcl')):
                            if len(i.get('ecl')) == 3 and i.get('ecl') in ecl_type:
                                if len(i.get('pid')) == 9 and re.match(r'\d{9}', i.get('pid')):
                                    count += 1
    
print(count)
