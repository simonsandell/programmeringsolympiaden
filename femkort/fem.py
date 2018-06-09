import fileinput

hasCol_A = {};
hasCol_B = {};


akort = [];
bkort = [];
i=0
for line in fileinput.input():
    sp = line.rsplit(" ")
    if (i<5):
        akort.append([sp[0],int(sp[1])]);
        hasCol_A[sp[0]] = True;
    if (i>4):
        bkort.append([sp[0],int(sp[1])]);
        hasCol_B[sp[0]] = True;
    i +=1;

startp= 0;
acheat = 0;
bcheat = 0;
for n in range(5):
    if (hasCol_A[akort[n][0]] == False):
        acheat =1;
    if (hasCol_B[bkort[n][0]] == False):
        bcheat = 1;
    if (akort[n][0] == bkort[n][0]):
        if (akort[n][1] > bkort[n][1]):
            startp = 0;
        else:
            startp =1;
    else:
        if startp == 0:
            hasCol_B[akort[n][0]] = False;
        else:
            hasCol_A[bkort[n][0]] = False;
if (startp == 0):
    print("A");
else:
    print("B");
if (acheat == 1 and bcheat == 1):
    print("A och B fuskar");
elif (acheat == 1):
    print("A fuskar")
elif (bcheat == 1):
    print("B fuskar")
