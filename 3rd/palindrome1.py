def row_pal(text,n): # 행에서 회문 수를 찾아주는 함수
    n_s = 0
    for i in range(8): #8행 반복
        for k in range(8-n+1): #회문인지 검사할 글자열의 처음 인덱스, +1의 의미: 그 인덱스 포함
            test_str=text[i][k:k+n]
            for m in range(n//2):
                if test_str[m]!=test_str[n-1-m]:
                    break
            else:
                n_s += 1
    return n_s
def col_pal(text,n): #열에서 회문 수를 찾아주는 함수
    n_s = 0
    for i in range(8):
        for k in range(8-n+1):
            test_str=''
            for l in range(n):
                test_str += text[k+l][i]
            for m in range(n//2):
                if test_str[m]!=test_str[n-1-m]:                   
                    break
            else:
                n_s += 1
    return n_s


for _ in range(10):
    n=int(input())
    text = []
    for __ in range(8):
        text += [input()]
    if n == 1:## 1짜리면 64반환
        print(f'#{_+1} 64')
    else:
        print(f'#{_+1} {row_pal(text,n)+col_pal(text,n)}')