def Sum(m,matrix,i,j):
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
    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            if Sum(m,mat,i,j)>max_fly:
                max_fly=Sum(m,mat,i,j)
    print(f'#{test_case} {max_fly}')

