t = int(input())

for test_case in range(1,t+1):
    puzzle=[]
    puzzleT=[[None,]*9 for _ in range(9)]
    d=1 # 겹치는 숫자가 있는지 없는지 체크하는 값
    for _ in range(9):
        puzzle +=[list(map(int, input().split()))]
    for i in range(9):
        for j in range(9):
            puzzleT[i][j]=puzzle[j][i] # 전치 행렬
    while True:
        for row in puzzle:
            for i in range(1,10):# 가로에 대해서
                if i in row: # 만약 숫자가 겹치면 반드시 빠지는 숫자가 있으므로
                    pass
                else:
                    d=0
                    break
        if d == 0:
            print(f'#{test_case} {d}') # 숫자가 겹치면 0 출력하고 반복문 종료
            break

        for row in puzzleT: # 세로에 대해서
            for i in range(1,10):
                if i in row:
                    pass
                else:
                    d=0
                    break
        if d == 0:
            print(f'#{test_case} {d}')
            break

        for i in range(0,9,3): # 9칸짜리 정사각형
            for j in range(0,9,3):
                for k in range(1,10):
                    if (k in puzzle[i][j:j+3]) or (k in puzzle[i+1][j:j+3]) or (k in puzzle[i+2][j:j+3]) :
                        pass
                    else:
                        d=0
                        break
        print(f'#{test_case} {d}')
        break