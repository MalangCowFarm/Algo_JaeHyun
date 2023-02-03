def muyaho(num_list):
    global m                            # m 사용하려고 ㅇㅇ
    if len(num_list) == 1:              # list 반갈 다하면 반환해야지?
        return num_list
    
    check = (len(num_list)+1) // 2      # 일단 문제는 3 2 로 나누니까
    print(check)
    list_1 = muyaho(num_list[:check])   # 그 행동을 반복
    list_2 = muyaho(num_list[check:])   # 그 행동을 반복
    print('#', list_2)
    fin_list = []                       # list 히스토리 저장소
    i, j = 0, 0                         # 변수 초기화, 이걸로 인덱스 건들거임

    while i < len(list_1) and j < len(list_2): # 인덱스 내에서 반복
        if list_1[i] < list_2[j]:              # 두개중 첫 값이 작은거를
            fin_list.append(list_1[i])         # 먼저 넣자
            i += 1                             # 넣었으면 그 인덱스 다음걸로 ㄱㄱ
        else:                                  # 오른쪽이 더크면 
            fin_list.append(list_2[j])         # ㅇㅇ 알지?
            j += 1
    fin_list += list_1[i:]
    # print('#' ,fin_list)
    fin_list += list_2[j:]
    # print(fin_list)
    if len(fin_list) < m:                      # 저장 수가 길이보다 작으면
        m -= len(fin_list)                     # 뭔 소리?
    else:
        print(fin_list[m-1])                   # 저장수가 크면 그때의 원소값 출력
        exit()                                 # 그리고 코드 자체를 종료
    return fin_list                             

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
muyaho(num_list)
print(-1)