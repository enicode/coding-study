t=int(input())
for case in range(1,t+1):
    n=int(input())
    matrix=[]
    matrix90=[[None]*n for _ in range(n)]
    matrix180=[[None]*n for _ in range(n)]
    matrix270=[[None]*n for _ in range(n)]
    for _ in range(n):
        matrix += [list(map(int,input().split()))] # 원본 행렬 입력 받기

    for i in range(n):
        for j in range(n):
            matrix90[j][n-1-i]=matrix[i][j]
            matrix180[n-1-i][n-1-j]=matrix[i][j]
            matrix270[n-1-j][i]=matrix[i][j]
    # 바뀐 행렬 저장

    print(f'#{case}')
    for i in range(n):
        for j90 in range(n):
            print(matrix90[i][j90],end="")
        print(end=' ')
        for j180 in range(n):
            print(matrix180[i][j180],end="")
        print(end=' ')
        for j270 in range(n):
            print(matrix270[i][j270],end="")
        print()
    # 바뀐 행렬 출력