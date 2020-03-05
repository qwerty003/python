m1,y1 = map(int,input().split())
#m2,y2 = map(int,input().split())

nyear = y1
nleap = (nyear//4)-(nyear//100)+(nyear//400)
nextDay = ((365*nyear-1)+nleap+4)%7
print(nextDay)
print(nleap)
