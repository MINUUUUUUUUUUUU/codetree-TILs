n = int(input())
arr = list(map(int,input().split()))
arr.sort()

for i in range(0,len(arr)): 
    if i%2 == 1:
        continue
    print(arr[int(i/2)],end=' ')