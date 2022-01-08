t=int(input())

for _ in range(t):

    length, times, id_o = map(int,input().split())
    list_ = list(map(int,input().split()))
    list_ += [None for _ in range(times)]
    length=length+times

    for i in range(times):
        id_i,num = map(int,input().split())
        for k in range(length-1,id_i,-1):
            list_[k] = list_[k-1]
        list_[id_i]=num

    print(f'#{_+1} {list_[id_o]}')