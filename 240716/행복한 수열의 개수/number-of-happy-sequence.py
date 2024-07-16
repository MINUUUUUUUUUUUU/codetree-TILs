n, m = map(int,input().split())
li = []
for i in range(n):
    li.append([int(t) for t in input().split()])

def happy_sequence(li,m):
    result = 0
    row_count = 0
    for k in range(0,len(li[0])):
        temp = li[k][0]
        for n in range(0,len(li[0])):
            if temp == li[k][n]:
                temp = li[k][n]
                row_count += 1
            else:
                temp = li[k][n]
                if row_count >= m:
                    result += 1
                    break
                row_count = 1

            if row_count >= m:
                result += 1
                break

    return result
               

print(happy_sequence(li,m))