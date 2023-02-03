import sys

n, m = map(int, input().split())
pocket_dict = {}

for i in range(1, n+1):
    pocket = sys.stdin.readline().rstrip()
    pocket_dict[str(i)] = pocket
    pocket_dict[pocket] = i

for _ in range(m):
    a = sys.stdin.readline().rstrip()
    print(pocket_dict[a])