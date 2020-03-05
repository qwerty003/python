# selection sort
lis = [9,2,3,5,0,7,3,4]
for x in range(0,len(lis)):
    m = x
    for y in range(x,len(lis)):
        if lis[y] <= lis[m]:
            m = y
    lis[x],lis[m] = lis[m],lis[x]
print(lis)