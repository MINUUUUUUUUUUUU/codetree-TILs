def lcm(a,b):
    return (a*b) / gcd(a,b)

def gcd(a,b):
    if b==0: 
        return a
    else:
        return gcd(b, a%b)

n = int(input())
li = list(map(int,input().split()))
temp = 1
for i in li:
    temp = lcm(temp,i)
print(int(temp))