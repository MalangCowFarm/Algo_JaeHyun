T = int(input())
for _ in range(T):
    bu=[[]*15 for _ in range(15)]
    a = int(input())
    b = int(input())
    for i in range(14):
        bu[0].append(i+1)
    for j in range(1,15): # 층

        for i in range(1,15): # 호
            bu[j].append(sum(bu[j-1][:i]))
    print(bu[a][b-1])
    
    