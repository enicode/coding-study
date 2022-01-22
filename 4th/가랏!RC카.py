#s=v*t+0.5*a*(t**2)
t=int(input())

for k in range(t):
    n=int(input())
    s=0
    v=0
    a=0
    #초기속도/가속도/이동거리=0
    for _ in range(n):
        caa =list(map(int,input().split()))

        if len(caa)==1:
            s+=v
        #변수가 하나만 들어올 때
        else:
            c=caa[0]
            a=caa[1]
            if c==1:
                s+=v+a
                v+=a
            elif c==2:
                if v<a:
                    v=0
                    #속도 감소 제한
                else:
                    s+=v-a
                    v-=a

    print(f'#{k+1} {s}')

