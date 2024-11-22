n = int(input())
arr = list(map(int,input().split()))
sorted_arr = []

for i in range(0,len(arr)): 
    sorted_arr.append(arr[i])
    if i%2 == 1:
        continue
    sorted_arr.sort()
    print(sorted_arr[int(i/2)],end=' ')