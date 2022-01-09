t=int(input())

for _ in range(t):

    length, times, id_o = map(int,input().split())
    list_ = list(map(int,input().split()))
    list_ += [None for _ in range(times)]
    length=length+times # 리스트의 길이는 원래 길이 + 추가할 숫자의 갯수
    
    for i in range(times):
        id_i,num = map(int,input().split())
        for k in range(length-1,id_i,-1):
            list_[k] = list_[k-1] # 마지막부터 추가할 위치까지 전부 index+1로 밈
        list_[id_i]=num # 빈 자리에 넣음

    print(f'#{_+1} {list_[id_o]}')