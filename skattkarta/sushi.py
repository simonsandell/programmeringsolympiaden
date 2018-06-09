"""
asdf
"""
import fileinput

DATA = []
i = 0

for line in fileinput.input():
    if i == 0:
        r = int(line)

    if i == 1:
        c = int(line)

        for rn in range(r):
            DATA.append([])

            for cn in range(c):
                DATA[rn].append(0)

    if i > 1:
        for x in range(c):
            DATA[i-2][x] = line[x]
    i += 1


POS = (0, 0)
VISITED = {POS:True}
RES = ""

while True:
    MOVE = DATA[POS[0]][POS[1]]

    if MOVE == r'<':
        NEW_POS = (POS[0], POS[1]-1)

        if NEW_POS in VISITED:
            RES = "cykel"

            break

    if MOVE == r'>':
        NEW_POS = (POS[0], POS[1]+1)

        if NEW_POS in VISITED:
            RES = "cykel"

            break

    if MOVE == r'v':
        NEW_POS = (POS[0]+1, POS[1])

        if NEW_POS in VISITED:
            RES = "cykel"

            break

    if MOVE == r'^':
        NEW_POS = (POS[0]-1, POS[1])

        if NEW_POS in VISITED:
            RES = "cykel"

            break

    if MOVE == r'A':
        RES = "sushi"

        break

    if MOVE == r'B':
        RES = "samuraj"

        break
    VISITED[NEW_POS] = True
    POS = NEW_POS


print(RES)
