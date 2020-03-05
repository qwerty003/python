def check(n):
    if n == 1:
        print("Hooray")
    elif (n*n-n)%(2*n-2)!=0:
        print("Boo")
    else:
        print("Hooray")
        doof(n)


def doof(n):
    arr = [[0 for i in range(0, n)] for j in range(0, n)]
    maax = 2*n-1;max_count = (n*n-n)/(2*n-2)-1;
    arr[0][0] = maax
    row_val = maax -1
    col_val = n - 1
    for danger in range(1,n):
        arr[0][danger] = row_val
        arr[danger][0] = col_val
        avail = [i for i in range(1, n)]
        avail.remove(danger)
        count = 0
        while count < max_count:
            i,j = generate(arr,avail)
            arr[i][j] = row_val;arr[j][i] = col_val
            avail.remove(i);avail.remove(j)
            count+=1
        row_val -= 1;col_val -= 1
    for x in range(0, n):
        for y in range(0, n):
            if x == y:
                print(maax,end=' ')
            else:
                print(arr[x][y], end=' ')
        print("\t")


def generate(arr,avail):
    for m in range(0,len(avail)):
        for n in range(m+1,len(avail)):
            if arr[avail[m]][avail[n]]==0:
                return avail[m],avail[n]


test = int(input())
for _ in range(0,test):
    N = int(input())
    check(N)




