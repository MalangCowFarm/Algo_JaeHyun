n = int(input())
dp = [0]* 1000001 # 최대 숫자가 10^6 이니 list는 10^6 + 1 만큼 만듭시다.


for i in range(2, n+1): # 0과 1은 없죠?
    b, c = 1000000, 1000000 # 1씩 뺀다면 최대값이 되겠죠
        
    a = dp[i-1] + 1 # 1을 뺀 경우 i-1번째 dp 
    if not(i % 2): # 2로 나눠진다면
        b = dp[i // 2] + 1 # i//2 번째 dp와 1을 더합니다
            
    if not(i % 3): # 3으로 나눠진다면
        c = dp[i // 3] + 1 # i//3 번째 dp와 1을 더합니다

    dp[i] = min(a, b, c)   # 그 중 최소값이 dp[i]가 되겠네요!
print(dp[n])