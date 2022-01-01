def add_or_sub(n, sum=0):   
    if n%2==0:
        sum -=n
    else: sum += n
    n -= 1
    if n == 0 :
        return sum
    return add_or_sub(n,sum)


t = int(input())
nums=[]

for _ in range(t):
    nums += [int(input())]


for _ in range(t):
   print(f'#{_+1} {add_or_sub(nums[_],)}') 