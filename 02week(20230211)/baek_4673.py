list_num=[] # 빈 리스트 생성

def self_num(n): # 셀프넘버 함수 생성
    num=list(str(n)) # 입력받은 수를 문자로 변환 후 list로 한자씩 쪼개기
    sum_=n # 원래 숫자를 미리 더해놓기
    
    for i in range(len(num)): # 숫자가 몇자리 인지 확인
        sum_+=int(num[i]) # 위에서 리스트로 만든 숫자 하나씩 정수형으로 더해주기
        
    return sum_ # 그 값을 반환

for i in range(1,10001): # 1부터 
    list_num.append(self_num(i)) #위에서 생성한 빈 리스트에 생성자가 있는 수 쌓기
    if i not in list_num: # 만약 셀프넘버라면 이 리스트에 없겠죠? 그것을 출력합니다.
        print(i)
