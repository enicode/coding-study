t = int(input())

for _ in range(t):
    n = input()
    x=1
    n_num = int(n)
    zero_nine=['0','1','2','3','4','5','6','7','8','9']# 숫자가 나오면 하나씩 지워나갈 리스트
    while True:
        xn_num=x*n_num
        xn_list=str(n_num*x)
        for s_num in xn_list:
            if s_num in zero_nine:
                zero_nine.remove(s_num)#숫자가 있으면 지움
        if zero_nine == []:# 리스트가 비면 중단
            break
        x=x+1
    print(f'#{_+1} {xn_num}')
    