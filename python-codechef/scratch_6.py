def ada():
    s, w1, w2, w3 = list(map(int, input().split()))
    if s >= w1+w2+w3:
        print("1")
    elif s >= w1+w2 or s >= w2+w3:
        print("2")
    else:
        print("3")



test = int(input())
for _ in range(0,test):
    ada()