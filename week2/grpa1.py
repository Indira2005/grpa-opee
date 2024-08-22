x1 = input("x1: ")
x2 = input("x2: ")

y1 = input("y1: ")
y2 = input("y2: ")
y3 = input("y3: ")

z = input("z: ")

x1, x2 = x2, x1
print(x1, x2, sep = " ")


y1, y2, y3 = y2, y3, y1
print(y1,y2,y3, sep = " ")

a = z
del z
print(a)