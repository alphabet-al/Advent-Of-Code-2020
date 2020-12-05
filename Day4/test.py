string = "A - 13, B - 14, C - 15"
  
# Converting string to dictionary 
Dict = dict((x.strip(), y.strip()) 
             for x, y in (element.split('-')  
             for element in string.split(', '))) 
  
print(Dict) 
print(Dict['A']) 
print(Dict['C']) 