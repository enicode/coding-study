t = int(input())
num_sets = []

for _ in range(t):  
    num_sets += [list(map(int, input().split()))]

odd_sum_set=[]

for num_set in num_sets:
    odd_sum=0
    for num in num_set:
        if num%2!=0:
            odd_sum += num
        else: pass
    odd_sum_set += [odd_sum]

for i in range(t) :
    print(f'#{i+1} {odd_sum_set[i]}')


