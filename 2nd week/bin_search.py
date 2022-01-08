t = int(input())
for _ in range(t):
    n=int(input())
    memory=[None for _ in range(n+1)]
    index = 1
    for i in range(1,n+1):
        while True:
            if 2*index <= (n) and 2*index+1 <=(n) :
                if (memory[int(2*index)] != None) : 
                    if (memory[int(2*index+1)] != None):
                        index=int(index/2)
                        continue
                    elif (memory[int(2*index+1)] == None):
                        memory[int(index)]=i
                        index=int(index*2+1)
                        break
                else: 
                    index= int(2*index)
                    continue
            elif 2*index <=n and 2*index+1 >(n):
                if (memory[int(2*index)] != None) : 
                    if memory[int(index)] == None:
                        memory[int(index)]=i
                        index=int(index/2)
                    else:
                        index=int(index/2)                   
                    break
                elif memory[int(2*index)] == None:
                    index=int(index*2)               
                    continue
            else:
                memory[int(index)]=i
                index=int(index/2)
                break
    print(f'#{_+1} {memory[1]} {memory[int(n//2)]}')
'''
for i in range(1,n+1):
    while True:
        if 2*index <= n(왼쪽 자식이 존재한다) and 오른쪽 자식도 존재한다.:
            if 왼쪽자식의 값이 있으면: 
                if 오른쪽 자식의 값이 있으면                
                    부모노드로
                elif 오른쪽 자식의 값은 없으면               
                    이터레이블을 자기에게 할당
                    인덱스를 오른쪽 자식으로
                    break

            elif 값이 없으면:
                인덱스를 왼쪽 자식으로
        if 2*index <= n(왼쪽 자식이 존재한다) and 오른쪽 자식은 없다.:
                if 왼쪽자식의 값이 있으면: 
                    이터레이블을 자기에게 할당
                    인덱스를 부모노드로
                break
            elif 값이 없으면:
                인덱스를 왼쪽 자식으로           
        else:
            자신에게 이터레이블 할당
            인덱스를 부모노드로
            break
'''