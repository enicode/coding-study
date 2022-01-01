t = int(input())
num_sets = []
#테스트 케이스 수 t, 숫자로 이루어진 리시트를 저장할 리스트 num_sets
for _ in range(t):  
    num_sets += [list(map(int, input().split()))]
# 숫자 리스트를 원소로 받는다
odd_sum_set=[]
#홀수 합만을 저장할 리스트 odd_sum_set
for num_set in num_sets:
    odd_sum=0
    for num in num_set:
        if num%2!=0:
            odd_sum += num
        else: pass
#num_sets 숫자들 중 홀수인것은 더하고 짝수인것은 더하지 않는다. 최종값을 odd_sum_set 에 저장
    odd_sum_set += [odd_sum]

for i in range(t) :
    print(f'#{i+1} {odd_sum_set[i]}')
# 순서대로 출력

