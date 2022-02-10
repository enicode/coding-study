def Sum(m,matrix,i,j): #파리채 크기, 매트릭스, 좌표가 들어오면 몇마리 잡히는지 돌려주는 함수
    s=0
    for l in range(m):
        for k in range(m):
            s += matrix[i+l][j+k]
    return s

t = int(input())

for test_case in range(1,t+1):
    n , m = map(int, input().split())
    mat = []
    for _ in range(n):
        mat += [list(map(int,input().split()))]
    max_fly=0
    for i in range(0, n-m+1):  # 파리채 크기를 고려하여 최대치까지 검색
        for j in range(0, n-m+1):
            if Sum(m,mat,i,j)>max_fly: 
                max_fly=Sum(m,mat,i,j) # 더 큰 값이 나오면 교체
    print(f'#{test_case} {max_fly}')

