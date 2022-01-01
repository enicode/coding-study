t = int(input())
pindex_sets = []

for _ in range(t):
    n = int(input())
    a = b = c = d = e = 0

    while n%2 == 0:
        a += 1
        n /= 2
    while n%3 == 0:
        b += 1
        n /= 3
    while n%5 == 0:
        c += 1
        n /= 5
    while n%7 == 0:
        d += 1
        n /= 7
    while n%11 == 0:
        e += 1
        n /= 11
    pindex_sets += [[a,b,c,d,e]]

for _ in range(t) :
    print(f'#{_+1} {pindex_sets[_][0]} {pindex_sets[_][1]} {pindex_sets[_][2]} {pindex_sets[_][3]} {pindex_sets[_][4]}')