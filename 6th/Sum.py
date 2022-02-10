for _ in range(10):
    test_case=int(input())
    matrix=[]
    for k in range(100):
        matrix += [list(map(int,input().split()))]
    
    m=-1
    for i in range(0, 100):
        s = sum(matrix[i])
        if m < s:
            m = s
    for i in range(0,100):
        s=0
        for j in range(0,100):
            s += matrix[j][i]           
        if m < s:
            m = s
    dig=0
    for i in range(0,100):
        dig+=matrix[i][i]
    if m < dig:
        m = dig
    print(f'#{test_case} {m}')

    # 그냥 행 합 다 검사, 열 합 다 검사, 대각 합 다 검사
