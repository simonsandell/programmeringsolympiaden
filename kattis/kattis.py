import time
import itertools
import matplotlib.pyplot as plt

# find the interval of x which can be seen from a certain point

def getSeeableInterval(n, H, X, Y, x, y):
    right_lim = X[-1]
    hy = H-y

    for i in range(n+1, len(X)):
        if X[i] > right_lim:
            break
        dy = Y[i] -y

        if (dy>0):
            chi = x+hy*(X[i] -x)/(dy)

            if chi < right_lim:
                right_lim = chi
    left_lim = 0

    for i in reversed(range(0, n)):
        if X[i] < left_lim:
            break
        dy = Y[i] -y

        if (dy>0):
            chi = x - hy*(x-X[i])/(dy)

            if chi > left_lim:
                left_lim = chi

    return (left_lim,right_lim)
    #return (int(0.5 + left_lim), int(-0.5 + right_lim))
#
# N number of wall points
# H y-distance of the wall
# X x-pos of wall points
# Y y-pos of wall points
# Z 1 or 0 if point must be covered
#
def kattis(N, H, X, Y, Z):
    print("function called")
    points_to_cover = []
    num_to_cover = 0
    cov_points = {}
    points_of_interest = set()
    # for each point we want to cover, get the x intervals (x_start, x_end)
    # on the wall from which it can be seen,
    # make set of points where we might want to place guards
    plt.plot(X, Y)
    plt.plot([X[0], X[-1]], [H, H])


    for i,x in enumerate(X):
        if Z[i] == 1:
            points_to_cover.append(X[i])
            cov_points[x] = getSeeableInterval(i, H, X, Y, x, Y[i])
            points_of_interest.add(cov_points[X[i]][0])
            points_of_interest.add(cov_points[X[i]][1])
    num_to_cover = len(points_to_cover)
    pts_seen_from_poi = {}

    dict_of_setlengths = {}
    pois_seeing_cov_pt = {}
    print("seeable intervals generated")

    for cp in cov_points:
        pois_seeing_cov_pt[cp] = set()


    for poi in points_of_interest:
        seen_from_this = set()
        doadd = True
        # determine which points can be seen from this poi

        for cov_pt in points_to_cover:
            if ((poi <= cov_points[cov_pt][1]) and (poi >= cov_points[cov_pt][0])):
                seen_from_this.add(cov_pt)
        # check if this set is subset of any other, if so, dont add

        for key in pts_seen_from_poi:
            if seen_from_this.issubset(pts_seen_from_poi[key]):
                doadd = False

        if doadd:
            pts_seen_from_poi[poi] = seen_from_this
            dict_of_setlengths[poi] = len(seen_from_this)

            for cov_pt_seen in seen_from_this:
                pois_seeing_cov_pt[cov_pt_seen].add(poi)
    print("pois pruned")

    list_of_setlengths = sorted(list(dict_of_setlengths.values()))
    max_cov = 0
    min_num_guards = 0

    while max_cov < num_to_cover:
        max_cov += list_of_setlengths[-1]
        del list_of_setlengths[-1]
        min_num_guards += 1


    n_guards = 0
    already_seen = set()

    while len(pois_seeing_cov_pt) > 0:
        print(len(pois_seeing_cov_pt))
        # get a point to be covered and the set of pois seeing that point
        cov_pt,poi_seeing_cov_pt = pois_seeing_cov_pt.popitem()
        already_seen.add(cov_pt)
        max_cov = 0;
        unseen_pts = set()
        # check which of those pois sees the most cov_pts

        for poi in poi_seeing_cov_pt:
            poi_new_unseen = pts_seen_from_poi[poi].difference(already_seen)
            n_poi_seen = len(poi_new_unseen)

            if n_poi_seen > max_cov:
                max_cov = n_poi_seen
                unseen_pts = poi_new_unseen
        already_seen = already_seen.union(unseen_pts)
        # remove cov_pts seen by try guard 

        for seen_pt in unseen_pts:
            del pois_seeing_cov_pt[seen_pt]
        n_guards += 1;

    return n_guards
