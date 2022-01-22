t=int(input())

for k in range(t):
    b_month=[1,3,5,7,8,10,12]
    s_month=[4,6,9,11]
    m1,d1,m2,d2 = map(int,input().split())

    a=0
    b=d1
    for i in range(m1, m2):
        if i in b_month:
            a+=31 #큰달을 지나면 31일 추가
        elif i in s_month:
            a+=30 #작은달을 지나면 30일 추가
        else:
            a+=28 #2월을 지나면 28일 추가

    print(f'#{k+1} {a-d1+d2+1}') # +1 : 1일에서 1일도 하루로 치나봄

