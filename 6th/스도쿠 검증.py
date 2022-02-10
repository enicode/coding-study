t = int(input())

for test_case in range(1,t+1):
    puzzle=[]
    puzzleT=[[None,]*9 for _ in range(9)]
    d=1
    for _ in range(9):
        puzzle +=[list(map(int, input().split()))]
    for i in range(9):
        for j in range(9):
            puzzleT[i][j]=puzzle[j][i]
    while True:
        for row in puzzle:
            for i in range(1,10):
                if i in row:
                    pass
                else:
                    d=0
                    break
        if d == 0:
            print(f'#{test_case} {d}')
            break

        for row in puzzleT:
            for i in range(1,10):
                if i in row:
                    pass
                else:
                    d=0
                    break
        if d == 0:
            print(f'#{test_case} {d}')
            break

        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range(1,10):
                    if (k in puzzle[i][j:j+3]) or (k in puzzle[i+1][j:j+3]) or (k in puzzle[i+2][j:j+3]) :
                        pass
                    else:
                        d=0
                        break
        print(f'#{test_case} {d}')
        break