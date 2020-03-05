def prime(num):
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                global b
                b = 1
                break
        else:
            global b
            b = 0

    else:
        global b
        b = 1


n = int(input())
b = 0
for a in range(2, n):
    if b > 0:
        break
    if n % a == 0:
        b = b+1
        continue
prime(a)
prime(b)
if b > 0:
    print(-1)
else:
    b = 0
    while n > 0:
        b = b+1
        n = n//2





