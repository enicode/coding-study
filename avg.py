t = int(input())
avg_list = []
for _ in range(t):
    num_list = list(map(int,input().split()))
    sum = 0
    for num in num_list:
        sum += num
    avg_list += [sum/10]

for _ in range(t):
    print(f'#{_+1} {avg_list[_]:.0f}')