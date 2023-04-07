word = input() # 문자열 받고
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 걸러낼 문자 리스트

for _ in range(len(word)): # 입력받은 문자열 길이 만큼 반복
    for i in cro: # 크로아티아 알파벳 리스트 순회
        if i in word: # 만약 입력받은 문자열에 있다면
            word=word.replace(i,'0') # 그 문자를 0으로 바꾸고
             
print(len(word)) # 길이 출력
    