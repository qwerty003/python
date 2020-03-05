def prog():
    count = 0;check0 = 0
    nx,ny = map(int,input().split())
    if nx*ny == 0:
        return count
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    x_positive = [];x_negative = [];y_positive = [];y_negative = []
    for p in x:
        if p>=0:
            x_positive.append(p)
        else:
            x_negative.append(p)
    for q in y:
        if q>=0:
            y_positive.append(q)
        else:
            y_negative.append(q)


    for y1 in y_positive:
        status = 0
        if y1 == 0:
            count += (ny-1)*nx
            check0 = 1
            continue
        for y2 in y_negative:
            for x1 in x:
                if x1**2 == y1 *y2 *(-1):
                    count+=1
                    status = 1
                    break
            if status:
                break

    # for horizontal triangles
    for x1 in x_positive:
        status = 0
        if x1 == 0 :
            if check0:
                count -= ny-1
                continue
            else:
                count += (nx-1)*ny
        for x2 in x_negative:
            for y1 in y:
                if y1 ** 2 == x1 * x2 *(-1):
                    count += 1
                    status = 1
                    break
            if status:
                break
    return count



test = int(input())
for _ in range(0,test):
	c = prog()
	print(c)