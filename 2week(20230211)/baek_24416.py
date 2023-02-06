def fib_one(n):
    global cnt
    if n == 1 or n == 2:
        cnt += 1
        return 1
    else:
        return fib_one(n - 1) + fib_one(n - 2)

def fib_two(n):
    global cnt2
    for i in range(3,n+1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())
f = [0, 1, 1] + [0] * 38
cnt, cnt2 = 0, 0

fib_one(n)
fib_two(n) # 사실상 n-2

print(cnt, cnt2)
