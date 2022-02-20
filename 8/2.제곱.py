def power(n,m): # n(밑)과 m(지수)를 입력 받아 거듭제곱 값을 돌려주는 함수
    if m == 0:
        return 1 # 지수가 0 이면 1을 돌려준다.
    elif m == 1:
        return n # 지수가 1이면 밑을 돌려준다.
    else:
        return n*power(n,m-1) # 지수가 1보다 크면 밑은 같고 지수가 1 작은 power 함수를 재귀 호출하고 n을 곱한 값을 돌려준다.

for _ in range(10):
    p=int(input()) # test_case 번호
    n,m = map(int, input().split()) #밑과 지수
    print(f'#{p} {power(n,m)}') # 거듭제곱 출력