import sys

sys.stdin = open("8\\input.txt", "r")


for test_case in range(10):
    case_number=int(input()) # 케이스 번호
    pw=list(map(int,input().split())) # 암호

    big_cycle=(min(pw)//15)
    pw = [pw[i]-[15*big_cycle for _ in range(8)][i] for i in range(8)]
    # 5와 8의 최소공배수는 40 이므로 숫자를 40회 뒤로 보내면 암호의 모든 숫자는 1+2+3+4+5=15 만큼 
    # 작아진 채로 원래 순서로 돌아간다. 
    # 따라서 암호의 모든 숫자에서 암호 숫자 중 (제일 작은 숫자를 15로 나눈 몫) 번 만큼 15를 빼주면 
    # 암호의 어떠한 수가 0이 되기 직전 암호의 상태를 알 수 있다.
    # 하지만 암호 숫자의 최솟값이 중복 된다든지 하면, 또 그 순서를 따져야 하므로 귀찮다. 한 번 더 8사이클 돌리는
    # 정도는 별차이 없을테니 (제일 작은 숫자를 15로 나눈 몫-1) 번 만큼 15를 빼주고 마지막에 16사이클을 돌린다.

    for i in range(0,80): # (16사이클 (16*5=80)
        pw[i%8] -= i%5+1 # 빼주는 수는 0 위치에서 1 부터 4위치에서 5까지 변하므로
        if pw[i%8] <= 0: # 만약 0보다 작아지는 숫자가 생기면
            pw[i%8] = 0 # 그 숫자를 0으로 두고
            break  # 반복문을 종료한다.
    fpw = pw[i%8+1:]+pw[:i%8+1] # 그 숫자는 맨 뒤로 보내로 보내고 그 숫자 뒤 부터 마지막 까지를 앞에 붙인다.
    p_fpw=' '.join(str(a) for a in fpw) # 숫자를 문자로 바꿈
    print(f'#{case_number} {p_fpw}' ) # 출력



