def Fractal(n,x,y,isZero,result):
    size=3**n

    if n==0: pass
    elif isZero :
        for i in range(size):
            for j in range(size):
                result[x+i][y+j]=' '
    elif n==1 :
        result[x][y]='*'
        result[x+1][y]='*'
        result[x + 2][ y] = '*'
        result[x][ y + 1] = '*'
        result[x + 1][ y + 1] = ' '
        result[x + 2][ y + 1] = '*'
        result[x][ y + 2] = '*'
        result[x + 1][ y + 2] = '*'
        result[x + 2][ y + 2] = '*'

    else:
        offset = 3**(n-1)
        Fractal(n - 1, x, y, False, result)
        Fractal(n - 1, x + offset, y, False,result)
        Fractal(n - 1, x + offset * 2, y, False, result)
        Fractal(n - 1, x, y + offset, False, result)
        Fractal(n - 1, x + offset, y + offset, True, result)
        Fractal(n - 1, x + offset * 2, y + offset, False,result)
        Fractal(n - 1, x, y + offset * 2, False, result)
        Fractal(n - 1, x + offset, y + offset * 2, False, result)
        Fractal(n - 1, x + offset * 2, y + offset * 2, False, result)

n=int(input())
result=[[' ']*n for _ in range(n)]
index=0

for i in range(1,9):
    if 3**i == n:
        index=i

Fractal(index,0,0,False,result)
for _ in range(n):
        print(*result[_],sep='')