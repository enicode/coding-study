import sys

sys.stdin = open("D3\input.txt", "r")


def numOfDeadlock(table):
    num=0
    for i in range(a):
        check=0
        for j in range(a):
            if check == 0:
                if table[i][j] == 1:
                    check=1
            else:
                if table[i][j] == 2:
                    num += 1
                    check = 0
    return num 



for test_case in range(1,11):
    a=int(input())
    inputTable=[[0]*a for _ in range (a)]

    for i in range(a):
        inputTable[i] = list(map(int, input().split()))

    testTable = [[0]*a for _ in range (a)]

    for i in range(a):
        for j in range(a):
            testTable[i][j]=inputTable[j][i]

    print(f'#{test_case} {numOfDeadlock(testTable)}')
    

# 리스트를 왼쪽에서 오른쪽으로 읽는다 2가 나오면 왼쪽으로 떨어지므로 무시 1이 나오면 반발 하므로 그 때 체크 다음에 2가 나오면 교착 
# 다시 리스트를 왼쪽에서 오른쪽으로 읽는다. 2가 나오면 지나온 교착 상태에 붙을테니 무시, 1이나오면 그 때 체크 다음에 2가 나오면 교착+1