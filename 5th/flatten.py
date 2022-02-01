for case in range(1,11):
    fnum=int(input())
    flist=list(map(int,input().split()))
    s=sum(flist) # 합계
    print(s)
    mid=s//100 #합계의 절반
    flist.sort(reverse=True) # 내림차순 정렬
    rnum=0
    for height in flist:
        if height > mid:
            rnum += height-mid
        else:
            break
    # 절반보다 큰 값들을 전부 더함
    if rnum<=fnum: # 만약 절반보다 큰 값들의 합이 주어진 횟수보다 작다면 평탄화 가능하다.
        if s%100==0:
            print(f'#{case} 0') # 합계가 100으로 나누어떨어지면 0차이
        else:
            print(f'#{case} 1') # 합계가 100으로 나누어 떨어지지 않으면 1 차이
    else:
        num=0 # 덤프 횟수 초기값
        i=0 # 인덱스
        max=flist[0] # 최고 높이 초기값
        min=flist[99] # 최저 높이 초기값
        while num<=fnum: # 덤프 횟수가 주어진 횟수보다 작은 동안 반복한다.
            while flist[i]==flist[i+1]: # 만약 옆 상자와 높이가 같다면 인덱스를 더 낮은 상자 높이를 찾아서 계속 옮긴다.
                i+=1
            flist[i]-=1 # 인덱스에 해당하는 상자에서 높이를 한 칸 내린다.
            num+=i+1 # 한 칸 내리는건 0부터 인덱스까지 모든 상자들을 한 칸씩 내려야하므로
        max=flist[i]+1 # 만약 횟수를 초과하면 바로 직전 높이가 최고 높이
        i=99 # 인덱스를 마지막에 가져다 놓음
        num=0 # 덤프 횟수 초기화
        while num<=fnum: #덤프 횟수가 주어진 횟수보다 작은 동안 반복한다
            while flist[i]==flist[i-1]: # 만약 옆 상자와 높이가 같다면 인덱스를 계속 더 높은 상자높이를 찾아서 움직인다.
                i-=1
            flist[i]+=1 # 상자의 높이를 한 칸 올린다.
            num+=100-i # 상자의 높이를 한칸 올리는데 필요한 덤프 횟수는 그 전까지 모든 칸들에 상자를 하나씩 놓아야하므로 
        min=flist[i]-1 #만약 횟수를 초과하면 바로 직전 높이가 최저 높이
        dif=max-min
        print(f'#{case} {dif}')
    

