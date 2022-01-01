t = int(input())
avg_list = []
# t로 테스트 케이스 수 받아오고 평균값을 순서대로 저장한 avg_list 생성
for _ in range(t):
    num_list = list(map(int,input().split()))
    sum = 0
    for num in num_list:
        sum += num
    avg_list += [sum/10]
#숫자 10개를 받아 다 더 한뒤 10으로 나눈값을 저장
for _ in range(t):
    print(f'#{_+1} {avg_list[_]:.0f}')
#소수점 첫째자리에서 반올림하여 표시