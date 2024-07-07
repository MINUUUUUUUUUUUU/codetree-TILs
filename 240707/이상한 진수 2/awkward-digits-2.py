n = input()

for i in range(0,len(n)):
    if int(n[i]) == 0:
        n = n[:i] + '1' + n[i+1:]
        break

result = int(n, 2)
print(result)