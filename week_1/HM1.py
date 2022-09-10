a = int(179)
b = a // 100
c = a // 10 % 10
d = a % 10
print(b + c + d)

a = int(150)
b = a % (60 * 24) // 60
c = a % 60
print(b, c)