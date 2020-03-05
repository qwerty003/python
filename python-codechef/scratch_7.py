def eq(arr,l,r):
    inc_status = 0;dec_status = 0
    inc_count = 0;dec_count = 0
    for x in range(l,r):
        if arr[x+1] >= arr[x]:
            dec_status = 0
            if inc_status == 0:
                inc_count += 1
                inc_status = 1
        else:
            inc_status = 0
            if dec_status == 0:
                dec_count += 1
                dec_status = 1
    if inc_count == dec_count:
        print("YES")
    else:
        print("NO")




N, T = map(int,input().split())
Arr = list(map(int, input().split()))
for _ in range(0,T):
    L , R = map(int,input().split())
    eq(Arr,L-1,R-1)