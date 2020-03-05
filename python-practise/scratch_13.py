def prog():
    n,k = map(int,input().split())
    elems = list(map(int, input().split()))
    give = [];recieve = []
    for x in range(0,n):
        giving = elems[x]%k
        if giving == 0:
            recieving = 0
        else:
            recieving = k - giving
        give.append(giving);recieve.append(recieving)
    r = sum(give);give_amt = 0;recieve_amt = sum(recieve)
    for y in range(0,n):
        give_amt += give[y]
        recieve_amt -= recieve[y]
        if give_amt >= recieve_amt:
            r2 = give_amt - recieve_amt
            r = min(r,r2)
    print(r)






test = int(input())
for _ in range(0,test):
	prog()