def Turning_point(num_list, start_index):
    tp= start_index
    for i in range(tp-1, 0,-1):
        if num_list[tp] < num_list[i] : 
            return i+1
    return 0

t = int(input())

for test_case in range(1,t+1):
    n=int(input())
    pre=list(map(int,input().split()))

    profit=0
    tp=n-1
    start_index = n-1
    while True:
        max_val=pre[start_index]
        tp = Turning_point(pre, start_index)
        for i in range(start_index-1, tp-1,-1):
            profit += max_val-pre[i]
        start_index=tp-1
        if start_index <1:
            break
        
    print(f'#{test_case} {profit}')



# 지금 산걸 언제 팔아야 가장 많이 남길 수 있는가? 이후로 가장 비쌀 때

# 최고값 이전 꺼는 최고값에 팔면, 최고값 이후의 최고값 까지는 이후의 최고값에... 반복

# 종료 조건은?? 리스트의 처음에 다다랐을 때

# 이익 계산법: 맨 뒤에서 시작한다. 맨 뒤에서 자기보다 큰 값을 찾을때까지 앞으로 거슬러 올라간다. 자기보다 큰 값을 찾으면 그 직전 까지 모든 값들과의 차이를 더한다. 

# 다시 찾아낸 값으로 부터 그 값보다 큰 값을 찾을 때 까지 앞으로 거슬러 올라간다. 
