import fileinput
import math

inp = fileinput.input().readline().rsplit(" ")
inp = [int(x) for x in inp]

mini = inp[0]
maxi = inp[1]

# maximal difference is mini - 1
# minimal difference is 0


def diff(diff, start_L):
    L = start_L -diff
    B = L + diff
    prod = L*B
    while  (prod < maxi):
        if prod > mini:
            return [L, B]
        L += 1
        B += 1
        prod = L*B
    return [-1, -1]

k = 0
while True:
    res = diff(k, math.floor(pow(mini,0.5)))
    if res[0] == -1:
        k += 1
    else:
        break

print(str(res[0]) + " " + str(res[1]))
