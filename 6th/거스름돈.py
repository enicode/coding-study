t = int(input())

for test_case in range(1,t+1):
    money_list={50000:0,10000:0,5000:0,1000:0,500:0,100:0,50:0,10:0} #튜플 생성
    n=int(input())
    for i in range(8):
        money = list(money_list.keys())[i]
        money_list[money] = n//money
        n -= (n//money)*money # 가장 큰 단위로 돈을 빼가면서...
    print(f'#{test_case}')
    print(*list(money_list.values()),sep=' ')
