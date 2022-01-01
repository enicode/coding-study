t = int(input())
big_months=[1,3,5,7,8,10,12]
small_months=[4,6,9,11]
list_=[]
# t로 테스트 케이스 수 받기
# 큰 달, 작은 달 구분
#년월일에 해당하면 년월일을 저장하고 해당하지 않으면 -1 을 저장하는 배열 list_생성
for _ in range(t):
    ymd=input()
    year=int(ymd[:4])
    month=int(ymd[4:6])
    day=int(ymd[6:])
    if month in big_months:
        if 1<=day<=31:
            list_ += [[ymd[:4],ymd[4:6],ymd[6:]]]
        else: list_ += [[-1]]
# 큰 달 일 경우 1~31일 이면 년, 월, 일 저장 아니면 -1 저장
    elif month in small_months:
        if 1<=day<=30:
            list_ += [[ymd[:4],ymd[4:6],ymd[6:]]]
        else: list_ += [[-1]]
#작은 달 일 경우 1~30일 이면 년, 월, 일 저장 아니면 -1 저장
    elif month == 2:
        if 1<=day<=28:
            list_ += [[ymd[:4],ymd[4:6],ymd[6:]]]
        else: list_ += [[-1]]
# 2월은 1~28일 이면 년, 월, 일 저장 아니면 -1 저장
    else: list_ += [[-1]]

# 1~12를 벗어나면 -1 저장

for _ in range(t):
    if list_[_] == [-1]:
        print(f'#{_+1} -1')
# 만약 리스트에 -1 이 저장 되어있으면 -1 출력
    else: 
        print(f'#{_+1} {list_[_][0]}/{list_[_][1]}/{list_[_][2]}')
# 만약 리스트에 연, 월, 일 이 저장 되어있으면 연, 월, 일을 출력