def print_stars(n):
    if n > 0:
        print(' '.join(['*'] * n))  
        print_stars(n - 1)          
        print(' '.join(['*'] * n))  

n = int(input())
print_stars(n)