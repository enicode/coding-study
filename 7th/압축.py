import sys

sys.stdin = open("7th\\input.txt", "r")

t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    i_str_list = [None for _ in range(n)]
    i_num_list = [None for _ in range(n)]
    
    for i in range(n):
        c1, c2 = input().split()
        i_str_list[i] = c1
        n_c2 = int(c2)
        i_num_list[i] = n_c2
    
    print(f'#{test_case}')

    o_str_list = []
    k=0 # 입력 문자리스트 인덱스 겸 숫자리스트 인덱스
    j=0 # 출력 문자리스트 인덱스
    while True  :
        if i_num_list[n-1] == 0:
            break

        if len(o_str_list) == 10 :
            print("".join(o_str_list))
            o_str_list = []

        if i_num_list[k] == 0 :
            k += 1

        o_str_list.append(i_str_list[k])
        i_num_list[k] -= 1
        j += 1
    print("".join(o_str_list))


# 입력 받는 방법: 
 
# 문자를 입력 받을 n칸 짜리 리스트을 생성, 숫자를 입력 받을 n칸짜리 리스트를 생성한다. 

# 문자와 숫자를 빈칸을 구분자로 하여 입력 받는다. N번 반복한다.

# 출력 받는 방법

# 출력할 출력 문자열을 담을 10칸 짜리 리스트를 생성한다.

# 입력 받은 문자 리스트의 맨 앞에 문자를 출력 문자열에 담는다. 입력받은 문자 리스트의 상대적 위치와 같은 위치에 있는 숫자 리스트의 값을 1감소 시킨다. 

# 숫자 리스트에 있는 값이 0 이 되거나 출력 문자열이 가득찰 때까지 반복한다. 

# 1. 숫자 리스트에 있는 값이 0 이 된 경우: 입력 문자 리스트의 다음으로 이동하여 반복한다.

# 2. 출력 리스트가 가득찬 경우: 출력 문자열을 출력하고, 출력 문자열을 비운다.(or 새로 생성한다.)

# 반복 중에 입력 문자 리스트의 마지막 문자에 대한 숫자 리스트 값이 0 이되면 출력 문자열을 출력하고 프로그램을 종료한다.