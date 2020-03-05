def prog():
    n = int(input());s = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for x in range(0,n):
        s += min(a[x],b[x])
    print(s)







test = int(input())
for _ in range(0,test):
	prog()