import sys
input = sys.stdin.readline

def ste(stair, step):
    dp = []
    dp.append(stair[0])
    for i in range(1,3):
        if i == 1:
            dp.append(max(dp[i-1]+stair[i],stair[i]))
            continue
        dp.append(max(dp[i-2]+stair[i], stair[i-1]+stair[i]))
    for i in range(3,step):
        dp.append(max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2]))
    print(dp[-1])

step = int(input())
stair = [int(input()) for _ in range(step)]
if step == 1:
    print(stair[0])
elif step == 2:
    print(sum(stair))
else:
    ste(stair, step)