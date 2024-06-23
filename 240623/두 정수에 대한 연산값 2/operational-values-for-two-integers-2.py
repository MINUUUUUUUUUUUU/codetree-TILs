x = 0
y = 0

def cal(a,b):
    global x,y
    if a>b:
        x = a*2
        y = b+10
    else:
        x = a + 10
        y = b * 2
    return 0                                                                                                                                                                                            

a,b = map(int,input().split())
cal(a,b)
print("{} {}".format(x,y))