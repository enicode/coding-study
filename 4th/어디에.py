def puzzle(opuzzle,n):
    pz=[None for _ in range(n)]    
    for j in range(n):
        pz[j]=opuzzle[j].replace(" ",'').split("0")
    return pz
# 연속된 1들의 배열을 반환하는 함수
def puzzlet(opuzzle,n):
    tpz=[None for _ in range(n)]    
    for l in range(n):
        string=''
        for m in range(n):
            string = string+opuzzle[m][l]
        tpz[l]=string.split('0')

    return tpz
#들어온 행렬의 전치행렬의 연속된 1들의 배열을 반환하는 함수

t=int(input())

for test_case in range(1, t+1):
    n,k=map(int,input().split())
    opuzzle=[None for _ in range(n)]
    for i in range(n):
        opuzzle[i]=input().replace(" ",'')
        #공백을 제거하고 받음
    pz=puzzle(opuzzle,n)
    tpz=puzzlet(opuzzle,n)
    cnt=0
    for l in range(n):
        cnt+=pz[l].count('1'*k)+tpz[l].count('1'*k)
    #1이 k개 연속된게 몇개나 들어있나 확인하고 더함

    print(f'#{test_case} {cnt}')

    