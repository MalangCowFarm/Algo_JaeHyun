import sys
input = sys.stdin.readline
# 함수 보기전에 저 밑으로 가죠 쭉쭉쭉!

def ste(stair, step): # 함수 인자? 로 stair list와 step을 받아요.
    dp = []           # 빈 list를 생성합시다.
    dp.append(stair[0]) # 첫 계단의 점수를 먼저 넣구요
    for i in range(1,3): # 1 2 이렇게 돌겠죠?
        if i == 1: # 만약 1이라면 (dp[0] + stair[1]), (stair[1]) 중 큰값의 점수를 더해요. dp[1]이 되겠네요.
            dp.append(max(dp[i-1]+stair[i],stair[i])) #dp[0]이란 0번째까지의 계단 점수의 합입니다.
            continue # 아래의 append 문은 실행하지 않겠죠 그것이 continue 니까..
        dp.append(max(dp[i-2]+stair[i], stair[i-1]+stair[i])) # 만약 2가 들어오면 
        # (dp[0] + stair[2]), (stair[1]+stair[2]) 중 큰값을 추가해줘요 그것이 dp[2]가 되겠네요!
    for i in range(3,step): # 자 본격적으로 쭉쭉 가봅시다. 3부터 step-1 까지 돌돌돌
        dp.append(max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2]))
        # (stair[i]+stair[i-1]+dp[i-3]), (stair[i]+dp[i-2]) 중 큰값 머시기 저시기...
        # 인덱스 상으로 (0번째까지 합과 2번째 3번째 계단을 밟았을때 경우) 또는 (1번째 계단까지의 합과 3번째 계단 밟았을때 경우)
        # 중 큰 값이 dp[3]이 되겠습니다.
    print(dp[-1]) # 마지막 계단이 끝났을때 dp[-1] 저장된 점수 중 가장 마지막 즉 끝날때의 값을 프린트하면
                  # 끝나겠네요. 우린 첫 계단부터 가장 큰값만 받아서 누적하며 계산했으니까요
                  # 이게 바로 dp 입니다. 한번 한 연산을 계속 사용하는거죠.

step = int(input()) #!!!!!여기!!!!! 계단 수를 받습니다.
stair = [int(input()) for _ in range(step)] # 각 계단마다의 점수를 받아요.
if step == 1: # 만약 계단 수가 1개 라면 주저할것 없죠?
    print(stair[0])
elif step == 2: # 두개라도 주저할것 없습니다.
    print(sum(stair))
else: # 여기서부터 문제입니다. 함수로 올라가보죠
    ste(stair, step)