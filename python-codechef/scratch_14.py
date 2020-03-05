def prog():
    Arr = [[0 for i in range(4)] for j in range(4)]
    for __ in range(0, int(input())):
        movie, slot = input().split()
        movie_index = ord(movie) - 65
        slot_index = int(slot) // 3 - 1
        Arr[movie_index][slot_index] += 1
    profit = -400
    lis = sorted([Arr[0][0], Arr[1][1], Arr[2][2], Arr[3][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[0][0], Arr[1][1], Arr[3][2], Arr[2][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[0][0], Arr[2][1], Arr[3][2], Arr[1][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[0][0], Arr[2][1], Arr[1][2], Arr[3][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[0][0], Arr[3][1], Arr[1][2], Arr[2][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[0][0], Arr[3][1], Arr[2][2], Arr[1][3]]);
    amt = amount(lis);
    profit = max(profit, amt)

    lis = sorted([Arr[1][0], Arr[0][1], Arr[2][2], Arr[3][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[1][0], Arr[0][1], Arr[3][2], Arr[2][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[1][0], Arr[2][1], Arr[3][2], Arr[0][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[1][0], Arr[2][1], Arr[0][2], Arr[3][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[1][0], Arr[3][1], Arr[0][2], Arr[2][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[1][0], Arr[3][1], Arr[2][2], Arr[0][3]]);
    amt = amount(lis);
    profit = max(profit, amt)

    lis = sorted([Arr[2][0], Arr[1][1], Arr[0][2], Arr[3][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[2][0], Arr[1][1], Arr[3][2], Arr[0][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[2][0], Arr[0][1], Arr[3][2], Arr[1][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[2][0], Arr[0][1], Arr[1][2], Arr[3][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[2][0], Arr[3][1], Arr[1][2], Arr[0][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[2][0], Arr[3][1], Arr[0][2], Arr[1][3]]);
    amt = amount(lis);
    profit = max(profit, amt)

    lis = sorted([Arr[3][0], Arr[1][1], Arr[2][2], Arr[0][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[3][0], Arr[1][1], Arr[0][2], Arr[2][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[3][0], Arr[2][1], Arr[0][2], Arr[1][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[3][0], Arr[2][1], Arr[1][2], Arr[0][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[3][0], Arr[0][1], Arr[1][2], Arr[2][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    lis = sorted([Arr[3][0], Arr[0][1], Arr[2][2], Arr[1][3]]);
    amt = amount(lis);
    profit = max(profit, amt)
    print(profit)
    return profit



def amount(liss):
    result = 0
    for x in range(0,4):
        if liss[x] == 0:
            result -= 100
        result += 25*(x+1)*liss[x]
    return result





test = int(input())
total = 0
for _ in range(0,test):
    total += prog()
print(total)