a, b= map(int,input().split())

mul=0
while True:
    if a%2==1:
        mul+=b
    a = a//2
    b = b*2
    if a==1:
        mul+=b
        break

print(mul)

