import sys

input = sys.stdin.readline
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)    

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    gcd(a, b)
    print(int(lcm(a, b)))
   