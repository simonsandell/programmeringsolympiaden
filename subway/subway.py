import fileinput

a = fileinput.input().readline().rsplit(" ")
print(a)
a = [ int(x) for x in a]

result = a[3]

while (a[2] > 0 and a[0] > 0):
    a[0] -= 1
    a[2] -= 1
    result += 1
if a[2]>0:
    result += a[2]
while (a[1] >1):
    a[1] -= 2
    result += 1
if (a[1] == 1):
    result += 1
    a[0] -= 2
while a[0] > 0:
    result += 1
    a[0] -= 4

print(result)


