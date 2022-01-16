t= int(input())

for _ in range(t):
    n, m=map(int,input().split(' '))
    ai= list(map(int,input().split()))
    bi= list(map(int,input().split()))
    max=0
    if n==m: ## 길이가 같으면 그냥 곱해서 반환
        for i in range(n):
            max += ai[i]*bi[i]

    elif n>m: ## a쪽이 길면 a를 한칸씩 밀어가면 비교
        for i in range(n-m+1):
            num_c=0
            for j in range(m):
                num_c += ai[i+j]*bi[j]
            if num_c>max:
                max=num_c
    else : ## b 쪽이 길면 b를 한칸씩 밀어가며 비교
        for i in range(m-n+1):
            num_c=0
            for j in range(n):
                num_c += bi[i+j]*ai[j]
            if num_c>max:
                max=num_c  

    print(f'#{_+1} {max}')