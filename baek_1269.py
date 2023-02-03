import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A_list = set(list(input().split()))
B_list = set(list(input().split()))

print(len(A_list -B_list) + len(B_list -A_list))
