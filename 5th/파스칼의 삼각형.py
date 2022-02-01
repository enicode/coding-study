t= int(input())

for case in range(1,t+1):
    n=int(input())
    if n == 1:
        pascal=[[1]]
    elif n==2:
        pascal=[[1],[1,1]]
    else:
        pascal=[[1],[1,1]]
        for i in range(2, n):
            tmp = [1]
            for j in range(0,i-1):
                tmp += [pascal[i-1][j]+pascal[i-1][j+1]]
            tmp += [1]
            pascal += [tmp]
    print(f'#{case}')
    for line in pascal:
        for num in line:
            print(num,end=" ")
        print()



