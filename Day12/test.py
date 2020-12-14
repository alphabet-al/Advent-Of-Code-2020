waypoint = 10 + 1j
x = 1
y = 1

e2 = 10

waypoint = waypoint + complex(0,e2)
print(waypoint.real, waypoint.imag)

x += waypoint.real * e2
print(x,y)