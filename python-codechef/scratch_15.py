def prog():
    count = 0
    nx,ny = map(int,input().split())
    if nx*ny == 0:
        return count
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    x_positive = [];x_negative = [];y_positive = [];y_negative = []
    for p in x:
        if p>0:
            x_positive.append(p)
        elif p<0:
            x_negative.append(p)
        else:
            x_positive.append(p)
            y_positive.append(p)
    for q in y:
        if q>0:
            y_positive.append(q)
        elif q<0:
            y_negative.append(q)
        else:
            x_positive.append(q)
            y_positive.append(q)
    x_positive = list(set(x_positive));y_positive = list(set(y_positive))
    nxp = len(x_positive);nxn = len(x_negative);nyp = len(y_positive);nyn = len(y_negative)

    #for vertical triangles

    for y1 in y_positive:
        if y1 == 0:
            count += (nyp + nyn -1)*(nxp + nxn -1)
            continue
        for x1 in x:
            for y2 in y_negative:
                if x1**2 == y1 *y2 *(-1):
                    count+=1;
                    break
    # for horizontal triangles

    for x1 in x_positive:
        if x1 == 0:
            continue
        for y1 in y:
            for x2 in x_negative:
                if y1 ** 2 == x1 * x2 *(-1):
                    count += 1;
                    break
    return count






test = int(input())
for _ in range(0,test):
	c = prog()
	print(c)