import sys

sys.stdin = open("8\\input (1).txt", "r")

t= int(input())

for test_case in range(1,t+1):
    memory=input() # 메모리
    count = int(memory[0]) 
    # 메모리의 첫번쨰 비트값이 처음에 고쳐야 하는지 아닌지 알려줌
    # 메모리 첫번째 비트값이 1 이라면 메모리를 전부 1로 고쳐쓰고 시작해야함

    for i in range (len(memory)-1): # 비트를 앞에서부터 훑으면서 본다.
        if memory[i] != memory[i+1]: # 지금 비트와 다음 비트 값이 다르면 고쳐야 하므로 count 1증가.
            count+=1 

    print(f'#{test_case} {count}')

