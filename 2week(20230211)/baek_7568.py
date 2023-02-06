import sys
input = sys.stdin.readline

n = int(input().strip())
list_body = [list(map(int, input().split())) for _ in range(n)]
rlt = []

for i in range(n):
    cnt = 1
    for j in range(n):
        if list_body[i][0] < list_body[j][0] and list_body[i][1] < list_body[j][1]:
            cnt += 1
    rlt.append(cnt)

print(*rlt)

