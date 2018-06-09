def getSeeableInterval(n,H,X,Y,x,y):
    right_lim = X[-1];
    hy = H-y;
    for i in range(n+1,len(X)):
        if X[i] > right_lim:
            break;
        dy = Y[i] -y;
        if (dy>0):
            chi = x+hy*(X[i] -x)/(dy);
            if chi < right_lim:
                right_lim = chi;
    left_lim = 0;
    for i in reversed(range(0,n)):
        if X[i] < left_lim:
            break;
        dy = Y[i] -y;
        if (dy>0):
            chi = x - hy*(x-X[i])/(dy);
            if chi > left_lim:
                left_lim = chi;
    return (left_lim,right_lim);

def getPointScore(p,scoreints):
    s = 0;
    for i in scoreints:
        if ((p<= i[1]) and (p >= i[0])):
            s +=1;
    return s;
def removeP(p,allints):
    rem = allints[:] 
    for i in range(len(allints)):
        if ((p<= allints[i][1]) and (p >= allints[i][0])):
            rem[i] = "remove";
    rem = [x for x in rem if x != "remove"];
    return rem;
def pickoutHighest(inter):
    pts = []
    pts[:] = [];
    hs = 0;
    hp = 0;
    for i in inter:
        pts.append(i[0]);
        pts.append(i[1]);
    pts = set(pts)
    for p in pts:
        pscore = getPointScore(p,inter);
        #print("score",pscore,"points",p);
        if pscore > hs:
            hs = pscore;
            hp = p;
    remaining = removeP(hp,inter);
    return remaining;


def placementStrategy(ints):
    res = 0;
    while len(ints)> 0:
        ints = pickoutHighest(ints);
        res +=1;
    return res
def getPointsSeeing(interval,pts):
    res = set();
    for p in pts:
        if ((p<= interval[1]) and (p >= interval[0])):
            res.add(p);
    return res;

def findHighScore(pts):
    max_s = 0;
    max_p = 0;
    for p in pts:
        if pts[p] > max_s:
            max_s = pts[p];
            max_p = p;
    return max_p

def removeHighest(inter,pts):
    max_p = findHighScore(pts);
    for i in inter.keys():
        if max_p in inter[i]:
            for p in inter[i]:
                pts[p] -= 1;
            del inter[i];




def placementStrat_2(ints):
    # make point list
    pts = {};
    for i in ints:
        pts[i[0]] = 0;
        pts[i[1]] =0;
    #for each interval, associate points
    idict ={};
    for i in ints:
         pts_seeing = getPointsSeeing(i,pts);
         idict[i] = pts_seeing;
         for p in pts_seeing:
             pts[p] +=1;
    guards = 0;
    while len(idict)>0:
        removeHighest(idict,pts);
        guards += 1;
    return guards;

def kattis(N, H, X, Y, Z):
    intervals = set();
    for i in range(len(X)):
        if Z[i] == 1:
            intervals.add(getSeeableInterval(i,H,X,Y,X[i],Y[i]));
    result = placementStrat_2(intervals);
    return result;
