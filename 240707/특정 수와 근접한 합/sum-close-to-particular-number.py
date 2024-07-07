n, s = map(int, input().split())
numbers = input().split()
numbers = [int(num) for num in numbers]
result = 0
for i in range(n):
    for j in range(n):
        if i==j : continue
        temp = sum(numbers) - numbers[i] - numbers[j]
        if abs(s - result) > abs(s - temp):
            result = temp

print(abs(s - result))