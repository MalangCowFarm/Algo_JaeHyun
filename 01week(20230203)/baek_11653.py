import sys
n = int(sys.stdin.readline())

n_list = []

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            n_list.append(i)
            n //= i
            break
for k in n_list:
    print(k)