#include <iostream>
//drop above when submitting
#include <vector>
#include <pair>
#include <unordered_map>

using namespace std;

pair<double,double> getSeeableInterval(int n,int H,int X[],int Y[],double x,double y){
    double right_lim = X[-1];
    double hy = H-y;
    double left_lim,dy,chi;
    for (int i=0, i< n+1, i++){
        if (X[i] > right_lim){
            break;
	}
        dy = Y[i] -y;
        if (dy>0){
            chi = x+hy*(X[i] -x)/(dy);
            if (chi < right_lim){
                right_lim = chi;
	    }
	}
    }
    left_lim = 0.0;
    for (int i=n-1,i >-1,i--){
        if (X[i] < left_lim){
            break;
	}
        dy = Y[i] -y;
        if (dy>0){
            chi = x - hy*(x-X[i])/(dy);
            if (chi > left_lim){
                left_lim = chi;
	    }
	}
    }
    return make_pair<double,double>(left_lim,right_lim);
}
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
        print(len(ints))
    return res
def getPointsSeeing(interval,pts):
    res = set();
    for p in pts:
        if ((p<= interval[1]) and (p >= interval[0])):
            res.add(p);
    return res;
set<double> getPointsSeeing(pair<double,double> interval,map<double,int> points){

}

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




	for (it=mymap.begin(); it!=mymap.end(); ++it)
		    std::cout << it->first << " => " << it->second << '\n';

int placementStrat_2(set<pair<double,double>> ints){
    // make point map
    map<double,int> pts;
    for (std::set<int>::iterator it=ints.begin(); it!=ints.end(); ++it){
    	pts.insert(par<double,int>(*it,0));
    }
    //for each interval, associate points
    map<pair<double,double>,set<double>> idict ={};
    set<double> pts_seeing;
    for (std::set<int>::iterator it=ints.begin(); it!=ints.end(); ++it){
         pts_seeing = getPointsSeeing(i,pts);
         idict[i] = pts_seeing;
         for p in pts_seeing:
             pts[p] +=1;
    guards = 0;
    while len(idict)>0:
        removeHighest(idict,pts);
        guards += 1;
    return guards;
}

int kattis(int N,int H,int X[],int Y[],int Z[]){
//find the intervals
	vector<pair<double,double>> intervals;	
	for (int i =0, i< (sizeof(X)/sizeof(*X)), i++){
		if (Z[i] == 1){
			intervals.add(getSeeableInterval(i,H,X,Y,X[i],Y[i]));
		}
	}
	//then, 


}
