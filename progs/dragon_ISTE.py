count = 0
position = 0
pace = 1
target = int(input())
if target<0:
    count = 1
    target = -1 * target
while position<target:
    position=position+pace*2
    count = count+1
print(count)

