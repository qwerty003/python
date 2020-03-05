def eq(arr,l,r):
    check = 0
    if r-l == 1:
        print("NO")
    else:
        for x in range(l+1, r):
            if (arr[x+1]-arr[x])*(arr[x]-arr[x-1]) < 0:
                check+=1
        if check%2 == 1:
            print("YES")
        else:
            print("NO")




N, T = input().split(' ')
T = int(T)
Arr = list(map(int, input().split()))
for _ in range(0,T):
    L , R = map(int,input().split())
    eq(Arr,L-1,R-1)