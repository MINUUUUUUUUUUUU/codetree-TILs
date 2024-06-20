def season(y,m,d):

    if m in [4,6,9,11]:
        if d > 30:
            return -1
    if m is 2:
        if (y%4==0 and y%100!=0 and d>29) or (y%400==0 and d>29):
            return -1
        elif (y%4 != 0 and d>28):
            return -1

    if m in [3,4,5]:
        return "Spring"
    elif m in [6,7,8]:
        return "Summer"
    elif m in [9,10,11]:
        return "Fall"
    elif m in [12,1,2]:
        return "Winter"
    return -1
        

y,m,d = map(int,input().split())
print(season(y,m,d))