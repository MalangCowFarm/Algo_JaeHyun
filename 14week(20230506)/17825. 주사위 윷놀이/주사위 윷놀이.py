def init_field():
    global field, scores
    scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 25, 22, 24,
    28, 27, 26, 30, 35] # 각 위치에서의 점수를 나타내는 리스트
    field = {} # 각 위치에서 이동 가능한 위치들을 나타내는 딕셔너리
    for i in range(21):
        lst = []
        for j in range(5):
            if i + j + 1 >= 21:
                lst.append(21) # 이동 가능한 위치가 21보다 큰 경우, 21로 이동
                break
            else:
                lst.append(i + j + 1)
        field[i] = lst

    root1 = [5, 22, 23, 24, 25, 31, 32, 20, 21] # 미리 지정된 위치들
    root2 = [10, 26, 27, 25, 31, 32, 20, 21]
    root3 = [15, 28, 29, 30, 25, 31, 32, 20, 21]

    for i in range(len(root1)):
        field[root1[i]] = root1[i + 1:i + 6] # 미리 지정된 위치에서 이동 가능한 위치들로 업데이트
        field[root3[i]] = root3[i + 1:i + 6]
        if i < 8:
            field[root2[i]] = root2[i + 1:i + 6]

def dfs(depth, score):
    global tenTurn, horses
    if depth == 10:
        return score

    dice = tenTurn[depth] # 현재 주사위 숫자
    max_score = score

    for i in range(4):
        if horses[i] == 21:
            continue # 이미 도착한 말은 제외
        next_index = 0
        if len(field[horses[i]]) < dice:
            next_index = 21 # 이동 가능한 위치가 없는 경우, 21(도착)로 이동
        else:
            next_index = field[horses[i]][dice-1] # 이동 가능한 위치 중 하나로 이동

        if next_index in horses and next_index != 21:
            continue # 다른 말이 이미 해당 위치에 있는 경우, 이동하지 않음

        cur_index = horses[i] # 현재 말의 위치 기록
        horses[i] = next_index # 말 이동
        max_score = max(max_score, dfs(depth + 1, score + scores[next_index])) # 다음 단계 탐색
        horses[i] = cur_index # 말 위치 원상 복구

    return max_score

tenTurn = list(map(int, input().split())) # 주사위의 결과를 입력받음
horses = [0, 0, 0, 0] # 각 말들의 위치
init_field() # field와 scores 변수 초기화
print(dfs(0, 0)) # 최대 점수 출력
