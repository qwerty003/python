x = input()
p = x.count('aaa')
q = x.count('aa')
r = x.count('a')
s = r - 2*q
n = len(x)
if p>0:
    req = -1
elif q>0:
    if s>0:
        req = (2*(n-2*q-s)+2)-2*q-s
    else:
        req = 2*(n-2*q)+2-2*q
elif r>0:
    req = 2*(n-r)+2-r
else:
    req = 2*n+2
print(req)