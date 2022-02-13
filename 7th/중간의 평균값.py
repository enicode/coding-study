import sys

sys.stdin = open("7th\\input.txt", "r")

t = int(input())

for test_case in range(1,t+1):
    num_list=list(map(int,input().split()))
    num_list.sort()

    middle_sum=0
    for i in range(1,9):
        middle_sum += num_list[i]

    print(f'#{test_case} {round(middle_sum/8)}')