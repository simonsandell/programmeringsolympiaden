"""
docstring
"""
import fileinput

for line in fileinput.input():
    DATA = line
DATA = DATA.rstrip("\n")
DATA = DATA.rsplit(" ")
RES = ""
NUM_LINES = len(DATA)

for i in range(NUM_LINES):
    x = DATA[i]
    cb = x.find(")")

    if (x[0] == "(" and cb != -1):
        RES += x[1:cb]+"("+x[cb:]
    elif x[0] == "(":
        RES += x[1:]+"("
    elif x[-1] == ")":
        RES += x[:-1]+")"

        if i < (NUM_LINES -1):
            RES += ", "
    else:
        RES += x + ", "
print(RES)
