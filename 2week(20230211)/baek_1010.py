import sys

def bri(L, R):
    if L == R:
        return 1
    else:
        
        return bri(L, R-1)

n = int(input())
for _ in range(n):
    L, R = map(int, sys.stdin.readline().split())

    
    

 # 2 2  1
 # 2 3  3
 # 2 4  6
 # 2 5  10