import matplotlib.pyplot as plt
import time
import itertools

def prepare_trials(num_to_cov, num_guards, big_dict,length_dict):
    for x in itertools.combinations(length_dict.keys(),num_guards):
        s = 0;
        for key in x:
            s+= length_dict[key]
        if s >= num_to_cov:
            act_cov = set()
            for key in x:
                act_cov = act_cov.union(big_dict[key])
            if len(act_cov) == num_to_cov:
                return num_guards
    return prepare_trials(num_to_cov, num_guards + 1, big_dict,length_dict)








# find the interval of x which can be seen from a certain point

def getSeeableInterval(n,H,X,Y,x,y):
    right_lim = X[-1]
    hy = H-y

    for i in range(n+1,len(X)):
        if X[i] > right_lim:
            break
        dy = Y[i] -y

        if (dy>0):
            chi = x+hy*(X[i] -x)/(dy)

            if chi < right_lim:
                right_lim = chi
    left_lim = 0

    for i in reversed(range(0,n)):
        if X[i] < left_lim:
            break
        dy = Y[i] -y

        if (dy>0):
            chi = x - hy*(x-X[i])/(dy)

            if chi > left_lim:
                left_lim = chi

    return (left_lim,right_lim)
#
# N number of wall points
# H y-distance of the wall
# X x-pos of wall points
# Y y-pos of wall points
# Z 1 or 0 if point must be covered
#
def kattis(N, H, X, Y, Z):
    points_to_cover = set()
    num_to_cover = 0
    cov_points = {}
    points_of_interest = set()
    # for each point we want to cover, get the x intervals (x_start,x_end)
    # on the wall from which it can be seen,
    # make set of points where we might want to place guards
    plt.plot(X,Y)
    plt.plot([X[0],X[-1]],[H,H])


    for i in range(len(X)):
        if Z[i] == 1:
            points_to_cover.add(X[i])
            cov_points[X[i]] = getSeeableInterval(i,H,X,Y,X[i],Y[i])
            points_of_interest.add(cov_points[X[i]][0])
            points_of_interest.add(cov_points[X[i]][1])
    num_to_cover = len(points_to_cover)
    print("generated seeableINtervals")
    pts_seen_from_poi = {}

    dict_of_setlengths = {}
    for poi in points_of_interest:
        seen_from_this = set()
        doadd = True;
        # determine which points can be seen from this poi
        for cov_pt in cov_points:
            if ((poi <= cov_points[cov_pt][1]) and (poi >= cov_points[cov_pt][0])):
                seen_from_this.add(cov_pt)
        # check if this set is subset of any other, if so, dont add
        for key in pts_seen_from_poi:
            if seen_from_this.issubset(pts_seen_from_poi[key]):
                doadd = False
        if doadd:
            pts_seen_from_poi[poi] = seen_from_this;
            dict_of_setlengths[poi] = len(seen_from_this)

    list_of_setlengths = sorted(list(dict_of_setlengths.items()))
    max_cov = 0;
    min_num_guards = 0;
    while max_cov < num_to_cover:
        max_cov += list_of_setlengths[-1]
        del list_of_setlengths[-1]
        min_num_guards += 1

    print(min_num_guards)


    # now, do bredden forst sokning av tradet
    # trials = [ [set(),n_guards],...]
    
    trials = prepare_trials(num_to_cover, min_num_guards, pts_seen_from_poi,dict_of_setlengths)
    return trials
"""
    for poi in pts_seen_from_poi:
        trials.append([poi])

    while True:
        # pick out first element and remove from list
        try_guards = trials[0]
        del trials[0]
        pts_covered = set()
        for g in try_guards:
            pts_covered = pts_covered.union(pts_seen_from_poi[g])

        print(try_guards)
        if pts_covered == points_to_cover:
            for g in try_guards:
                plt.plot(g,H,'bo')
            plt.show()
            return len(try_guards)
        else:
            for poi in pts_seen_from_poi:
                if not poi in try_guards:
                    new_guards = try_guards.copy()
                    new_guards.append(poi)
                    trials.append(new_guards)
"""
