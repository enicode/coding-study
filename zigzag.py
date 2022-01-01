def add_or_sub(n, sum=0):   
    if n%2==0:
        sum -=n
    else: sum += n
# 짝수면 뺴고 홀수면 더한다
    n -= 1
# 판단할 숫자의 값이 1 줄어듬
    if n == 0 :
        return sum
# 0에 도달하면 그 때까지 계산한 값을 리턴
    return add_or_sub(n,sum)
# 아니면 재귀함수 호출

#숫자 n이 입력되면 1부터 n까지 지그재그 값을 알려주는 재귀함수

t = int(input())
nums=[]
#테스트 케이스 수 t, 숫자들을 저장할 리스트 nums
for _ in range(t):
    nums += [int(input())]


for _ in range(t):
   print(f'#{_+1} {add_or_sub(nums[_],)}') 
#순서대로 출력한다.