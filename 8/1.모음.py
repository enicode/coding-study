t = int(input())

for test_case in range(1, t+1):
    words=input() # 단어를 입력 받는다.
    wrds='' # 모음이 없는 단어가 될 빈 문자열
    for alphabet in words: # 단어안의 알파벳에 대하여 순서대로
        if 'a'== alphabet or 'e'== alphabet or 'i'== alphabet  or 'o'== alphabet or 'u'== alphabet:
            pass # 모음이면 넘어가고
        else: 
            wrds+=alphabet # 모음이 아니면 wrds 에 추가한다.
    print(f'#{test_case} {wrds}') # 출력한다.