#возможно оно не самое читаемое, но рабочее (вроде) и своё...

#1 Вывод (std out)
a = 1, "new", 8, "old"
for i in range(len(a)):
    print(a[i], end='')

#2 Арифметика
from math import sqrt

x1 = 0
y1 = 0
x2 = 1
y2 = 1
print(sqrt((x2 - x1) ** 2 + ((y2 - y1) ** 2)))

#3 Списки
a = [0.1,"зеленый", 1.6, "белый", 0.3, "черный", 7, "2.0"]
flt = []

for i in range(len(a)):
    if type(a[i]) == float:
        flt.append(a[i])
print(sum(flt))

#4
a = ["красный","зеленый","белый" ,"черный"]
i = 0

while i in (0, -1):
    print(a[i])
    i -= 1

#5
element = 1
lst = [1, 5, 8, 3]
a = False

while element in lst:
    a = True
    break
if a == False:
    print('Clear')
else:
    print('Element', element, 'was found')

#6
lstt = ["9", "caMii", " /\y4LLIii", "proger", "v", "2022", "roDy"]
i = 0

while i in range(len(lstt)):
    a = lstt[i]
    i += 1
    b = a + ' '
    print(b, end='')

#7
lst1 = ["White", "Black", "Red"]
lst2 = ["Red", "Green", "White"]
i = 0

while i < (len(lst1)):
    e = lst1[i]
    b = lst2[i]
    i += 1
    print(e, b)

#8
a = ["a", "b", "c", "d"]
i = 0

while i in range(len(a)):
    b = a[i]
    c = (i + 1) * 3
    i += 1
    print(b * c, end='')

#9
s = [["a", "b", 1, 2.4], "string", ["new", 11111, 1000.0, "old"]]

integers = []
floats = []
strings = []

for i in range(len(s)):
    if type(s[i]) == list:
        for j in range(len(s[i])):
            n = s[i]
            s.append(n[j])

for i in range(len(s)):
    if type(s[i]) == int:
        integers.append(s[i])

    elif type(s[i]) == float:
        floats.append(s[i])

    elif type(s[i]) == str:
        strings.append(s[i])

print(integers)
print(floats)
print(strings)

#10
from time import gmtime, strftime
now_time = strftime("%a %b %d %H:%M:%S %Y", gmtime())
print(now_time)