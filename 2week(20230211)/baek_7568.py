import sys
input = sys.stdin.readline

n = int(input().strip())
list_body = [list(map(int, input().split())) for _ in range(n)]
rlt = []

for i in range(n): # 자 for문 돌돌 돌돌 돌돌 돌돌
    cnt = 1        # cnt 1로 한 이유는 자기 자신 1명은 추가를 해야하니까요!
    for j in range(n):  # 다시한번 돌립니다. 2중 for문이 되겠죠
        if list_body[i][0] < list_body[j][0] and list_body[i][1] < list_body[j][1]:
            cnt += 1 # 현재(i) 인덱스의 정보 보다 다음(j) 인덱스의 정보가 크다면 cnt 합니다.
                     # 사람 수를 세는겁니다. 비기면 cnt는 올라가지 않고 등수로 반환되겠죠. 
    rlt.append(cnt)

print(*rlt)

