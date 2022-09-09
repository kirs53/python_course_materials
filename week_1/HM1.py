a = int(179)
b = a // 100
c = a // 10 % 10
d = a % 10
print(b + c + d)

n = int(150)
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)