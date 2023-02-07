n = int(input())
num_list = list(map(int, input().split()))

dp = [] # 이제 이곳은 연속합의 집합소 입니다!
dp.append(num_list[0]) #0번째 인덱스는 일단 들어가야죠!

for i in range(1, n): # 위에서 0번째 사용했으니 1번부터 돌려줍니다!
    dp.append (max(dp[i-1]+num_list[i], num_list[i]))
# (dp 의 0번째 인덱스와 num_list의 1번 인덱스의 합), (num_list의 1번인덱스)중 큰걸 dp에 저장합니다!
# 반복문이 돌겠죠? 자.. 연속합이 큰것은 큰것대로 계속 갈것이고 아니라면 num_list의 i번째 값이 저장되는걸 반복합니다!

print(max(dp)) # 그리고 그 집합(list)에서 가장 큰값을 뽑으면 그것이 바로 답이랍니다.