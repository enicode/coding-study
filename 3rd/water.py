t= int(input())

for _ in range(t):
    p, q, r, s, w = map(int,input().split(' '))
    fa=p*w
    if w>r:
        fb=s*(w-r)+q
    else:
        fb=q

    if fa>=fb:
        print(f'#{_+1} {fb}')
    else:
        print(f'#{_+1} {fa}')