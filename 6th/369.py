n= int(input())
i=1
while i<=n:
    c= str(i)
    num = c.count('3')+c.count('6')+c.count('9') #숫자에 들어있는 3, 6, 9 숫자 세기
    if num !=0: # 숫자에 3, 6, 9 가 들어있다면 
        for _ in range(num):
            print('-',end='') # 그 숫자만큼 - 출력
        print(" ",end='')
    else:
        print(c,end=' ') # 아니면 숫자 출력
    i+=1