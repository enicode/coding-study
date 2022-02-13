import sys

sys.stdin = open("7th\\input.txt", "r")

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

# 종료 조건은?? 리스트의 마지막에 다달았을 때, 최고값을 더 이상 찾을 수 없을 때

# 이익 계산법: 최고값을 찾으면서 앞 값들을의 현재 최고값이라고 생각되는 가격에서 빼서 더해준다.
