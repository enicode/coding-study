t= int(input())

for _ in range(t):
    n=input()
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-1-i]: # 비교하다 다른게 나오면 다음을 실행
            print(f'#{_+1} {0}')
            break
    else:
        print(f'#{_+1} {1}') # 다른게 없다면 실행