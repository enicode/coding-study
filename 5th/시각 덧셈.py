t= int(input())
tm=[]
for case in range(1,t+1):
    tm=list(map(int,input().split()))
    h=tm[0]+tm[2]
    m=tm[1]+tm[3]

    if m>=60:
        m-=60
        h+=1
    if h>12:
        h-=12

    print(f'#{case} {h} {m}')