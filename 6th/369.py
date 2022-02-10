n= int(input())
i=1
while i<=n:
    c= str(i)
    num = c.count('3')+c.count('6')+c.count('9')
    if num !=0:
        for _ in range(num):
            print('-',end='')
        print(" ",end='')
    else:
        print(c,end=' ')
    i+=1