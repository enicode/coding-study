import sys
sys.stdin = open('D3\input (1).txt', "r")

def palin(number):
    test_str=str(number)
    if test_str[len(test_str)::-1] == test_str :
        return True
    else: 
        return False


t=int(input())
for test_case in range(t):
    a, b =map(int,input().split())
    num_list= [ x for x in range(32) if a<=x**2<=b]
    num_pal=0

    for number in num_list:
        if palin(number)&palin(number**2):
            num_pal +=1
    print(f'#{test_case+1} {num_pal}')
