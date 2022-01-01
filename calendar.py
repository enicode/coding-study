t = int(input())
big_months=[1,3,5,7,8,10,12]
small_months=[4,6,9,11]

list_=[]
for _ in range(t):
    ymd=input()
    year=int(ymd[:4])
    month=int(ymd[4:6])
    day=int(ymd[6:])
    if month in big_months:
        if 1<=day<=31:
            list_ += [[ymd[:4],ymd[4:6],ymd[6:]]]
        else: list_ += [[-1]]

    elif month in small_months:
        if 1<=day<=30:
            list_ += [[ymd[:4],ymd[4:6],ymd[6:]]]
        else: list_ += [[-1]]

    elif month == 2:
        if 1<=day<=28:
            list_ += [[ymd[:4],ymd[4:6],ymd[6:]]]
        else: list_ += [[-1]]

    else: list_ += [[-1]]

for _ in range(t):
    if list_[_] == [-1]:
        print(f'#{_+1} -1')
    else: 
        print(f'#{_+1} {list_[_][0]}/{list_[_][1]}/{list_[_][2]}')