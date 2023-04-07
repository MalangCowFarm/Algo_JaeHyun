n,m=map(int,input().split())
cards = list(map(int,input().split()))
sum_=[] # 3개 숫자를 합했을때 m 이하의 수를 넣을 빈 리스트 생성
for i in cards: # 리스트를 순회
    for j in range(cards.index(i)+1,n): #리스트에서 뽑은 숫자의 인덱스 다음부터 순회
        for k in range(j+1,n): # 그 위 for문 다음부터 순회
            if i+cards[j]+cards[k] <= m: # 만약 3개의 숫자 합이 m보다 작거나 같다면
                sum_.append(i+cards[j]+cards[k]) # 리스트에 추가
      
print(max(sum_)) # 리스트 값중 가장 큰 값이 정답.