import fileinput

for line in fileinput.input():
    data = line;
data = data.rstrip("\n")
data = data.rsplit(" ");
result = "";
ns= len(data);
for i in range(ns):
    x = data[i];
    cb = x.find(")");
    if (x[0] == "(" and cb != -1):
        result += x[1:cb]+"("+x[cb:]
    elif (x[0] == "("):
        result += x[1:]+"(";
    elif x[-1] == ")":
        result += x[:-1]+")";
        if (i < (ns -1)):
            result += ", ";
    else:
        result+= x + ", ";
print(result)
