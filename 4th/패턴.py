t=int(input())

for test_case in range(1,t+1):
    string=input()
    l=0
    for i in range(1, 11):
        if string[:i]==string[i:2*i]:
        #마디 길이 1~10 마다 같은지 안같은지 확인 같으면 멈추고 그 숫자가 마디 길이
            l=i
            break           

    print(f'#{test_case} {l}')