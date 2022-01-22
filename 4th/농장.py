t=int(input())

for test_case in range(1, t+1):
    n=int(input())
    fd=[None for _ in range(n+1)]
    for i in range(1,n+1):
        fd[i]=input()
    val=0
    mid=((n+1)//2)
    for k in range(1,mid):
        val+=sum(map(int,fd[k][mid-k:mid+(k-1)]))
        ##중앙전까지 합

    val+=sum(map(int,fd[mid]))
    ##중앙 합

    for k in range(mid+1,n+1):
        val+=sum(map(int,fd[k][mid-(n+1-k):mid+(n-k)]))
        ##중앙 다음 합

    print(f'#{test_case} {val}')