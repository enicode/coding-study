for test_case in range(1,11):
    length=int(input()) #암호 길이
    pw=input().split() #암호를 리스트로 받는다
    n=int(input()) # 명령어 수
    ics=input().split() # 명령어를 리스트로 받는다
    p=0 # 명령어 리스트에서 실행해야할 명령어의 위치
    num_cc=0 #실행한 명령어의 갯수
    while num_cc <n: # 실행한 명령의 갯수가 명령어 수 를 넘지 않을 때 까지 아래의 작업을 반복한다.
        if ics[p] == 'I':
            x = int(ics[p+1]) # x 위치
            y = int(ics[p+2]) # y 개
            ins_pos = x # 삽입할 위치는 X위치 바로 다음이므로 리스트에서는 x
            pw = pw[:ins_pos] + ics[p+3:p+3+y] + pw[ins_pos:] 
            # x위치를 자른다.
            # 입력할 y개의 숫자는 ics[p+3] 부터 ics[p+3+y-1] 까지 n개의 숫자이다. 
            # 자른 위치 뒤에 y개의 숫자를 붙여주고, 그 뒤에 잘라낸 자리 뒤쪽 암호를 붙인다.
            p = p+3+y # 다음 실행할 명령어의 위치(리스트의 y개의 숫자 다음 원소)
            num_cc+=1 # 실행한 명령어의 갯수를 1 늘린다.
        elif ics[p] == 'D':
            x = int(ics[p+1])
            y = int(ics[p+2])
            del_pos = x # 삭제를 시작할 위치는 X위치 바로 다음이므로 리스트에서는 x
            pw= pw[:del_pos] + pw[del_pos+y:] 
            # 삽입 때와 같이 암호를 자르는데 x위치 에서 잘르고 x+y 위치에서 한 번 더 자른다. 
            # 사이의 y개의 숫자는 버리고 암호를 연결한다.
            p = p+3
            num_cc+=1
        else:
            y=int(ics[p+1])
            pw = pw + ics[p+2:p+2+y+1] # y개의 숫자를 덧 붙인다.
            p= p+2+y
            num_cc+=1
    
    print(f'#{test_case} {" ".join(pw[0:10])}') #출력
