x = input()
start = x[0]
end = len(x)-1
length = len(x)
if
if start != 'a':
    n = 2
else:
    if x[1]!= 'a':
        n = 1
    else:
        n = 0
for k in range(0,len(x)):
    if x[k] != 'a':
        n+=2
    elif x[k] == 'a':
        if x[k-1] != 'a':
            n+=1
        else:
            n-=1
print()
