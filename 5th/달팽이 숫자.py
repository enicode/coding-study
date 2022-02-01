t=int(input())
sizes=[]
for case in range(1, t+1):
    sizes += [int(input())]

for case in range(t):
    snail_matrix=[[None]*sizes[case] for _ in range(sizes[case])]
    dim=sizes[case]
    i = 0
    j = 0
    num=1
    snail_matrix[i][j]=num
    num+=1
    while num <= dim**2:
        while (j<dim-1) and (snail_matrix[i][j+1]==None):
            snail_matrix[i][j+1]=num
            j+=1
            num+=1
    # 오른쪽 으로
        while (i<dim-1) and (snail_matrix[i+1][j]==None):
            snail_matrix[i+1][j]=num
            i+=1
            num+=1
    # 아래로
        while (j>0) and (snail_matrix[i][j-1]==None):
            snail_matrix[i][j-1]=num
            j-=1
            num+=1
    # 왼쪽으로
        while (i>0) and (snail_matrix[i-1][j]==None):
            snail_matrix[i-1][j]=num
            i-=1
            num+=1
    # 위로
    print(f'#{case+1}')
    for i in range(dim):
        for j in range(dim):
            print(snail_matrix[i][j],end=" ")
        print()