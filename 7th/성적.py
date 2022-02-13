def Total(m,f,a):

    return 35*m+45*f+20*a

t = int(input())

for test_case in range(1,t+1):
    n, k = map(int, input().split())

    score_dict={}
    for i in range(1,n+1):
        m,f,a=map(int, input().split(' '))
        score_dict[i] = Total(m,f,a)

    sorted_score_dict = sorted(score_dict.items(), key=lambda x:x[1])
    g_index=sorted_score_dict.index((k,score_dict[k]))+1

    print(f'#{test_case}',end=' ')
    if g_index <= n/10 :
        print('D0')
    elif g_index <= 2*(n/10) :
        print('C-')
    elif g_index <= 3*(n/10) :
        print('C0')
    elif g_index <= 4*(n/10) :
        print('C+')
    elif g_index <= 5*(n/10) :
        print('B-')
    elif g_index <= 6*(n/10) :
        print('B0')
    elif g_index <= 7*(n/10) :
        print('B+')
    elif g_index <= 8*(n/10) :
        print('A-')
    elif g_index <= 9*(n/10) :
        print('A0')
    else:
        print('A+')


# 테스트 케이스를 {번호:점수} 딕셔너리 형태로 받는다.
# 점수로 정렬한다.
# 번호의 위치를 찾는다.
# 위치에 따라 성적을 출력한다.
 