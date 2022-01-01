t = int(input())
pindex_sets = []
#테스트 케이스 수 t
#소인수분해 지수값들을 순서대로 저장할 배열 pindex_sets생성
for _ in range(t):
    n = int(input())
    a = b = c = d = e = 0
#모든 지수 값들 0 으로 초기화
    while n%2 == 0:
        a += 1
        n /= 2
#2로 나눌수 없을 때 까지 나누고 지수값 저장
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
# 배열에 순서대로 지수값 저장

for _ in range(t) :
    print(f'#{_+1} {pindex_sets[_][0]} {pindex_sets[_][1]} {pindex_sets[_][2]} {pindex_sets[_][3]} {pindex_sets[_][4]}')
# 순서대로 출력