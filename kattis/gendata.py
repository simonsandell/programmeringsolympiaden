import random
random.seed();

of = open("./input.in","w");
N = random.randint(3,pow(10,5));
H = random.randint(1,pow(10,6));
x_old = 0;
of.write(str(N)+" "+str(H)+"\n");
of.write("0 0 " +str(random.randint(0,1))+"\n");
for i in range(N-2):
    x = random.randint(0,10);
    y = random.randint(0,H);
    z = random.randint(0,1);
    of.write(str(x+x_old)+" "+str(y)+" "+str(z)+"\n");
    x_old += x;
xmax = x_old + random.randint(0,10);
of.write(str(xmax)+" 0 "+str(random.randint(0,1))+"\n");
