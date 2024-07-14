n = int(input())
li = []
for i in range(n):
    li.append([int(t) for t in input().split()])

def sum_coin(li,a):
    result = 0
    for i in range(0,3):
        for j in range(0,3):
            result = result + li[a[0]+i][a[1]+j]
    
    return result

t = [0,0]
great_result = 0
for i in range(0,n-2):
    t[0] = i
    for j in range(0,n-2):
        t[1] = j
        if sum_coin(li,t) > great_result :
            great_result = sum_coin(li,t) 

print(great_result)