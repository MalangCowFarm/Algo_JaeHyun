n = int(input())

for _ in range(n): # 일단 테케 만큼 for문을 돌려줘요! 돌돌돌
    words = input() # 입력.

    while '()' in words: # 저는 while 좋아합니다. 우선 문제가 원하는건 ()가 짝이 맞게 있는지 보는거죠?
        words = words.replace('()', '') # () 가 다 공백으로 바뀔때 까지 지워줍시다!

    if len(words):  # 만약 words라는 문자열에 하나라도 남는다면 그것은 땡!이겠죠
        print('NO')
    else:           # 다 지워졌다면 그것은 YES가 되겠습니다.
        print('YES')
