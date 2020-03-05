test = int(input())
for a in range(0,test):
    prime=[]
    num = int(input())
    for x in range(2, num+1):
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                if num % x == 0:
                    prime.append(x)
    print(len(prime))
    for b in prime:
        print(b,end=" ")
    print('\n')




