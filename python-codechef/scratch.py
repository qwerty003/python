def dora(n,m,arr):
    req = n * m
    if n<3 or m<3:
        print(req)
    else:
        for x in range(1, n - 1):
            current = 0
            for y in range(0, m - 2):
                current += 1
                pre = current - 1;nex = current + 1
                top = x -1;bottom = x + 1
                while (pre >= 0 and nex < m and top >= 0 and bottom < n) and(arr[x][pre] == arr[x][nex] and arr[top][current] == arr[bottom][current]):
                    req += 1
                    pre -= 1;nex += 1
                    top -= 1;bottom += 1
        print(req)


test = int(input())
for _ in range(0,test):
    N, M = [int(i) for i in input().split()]
    Arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        Arr.append(temp)
    dora(N,M,Arr)