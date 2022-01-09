class cQueue():
    def __init__(self, size):
        self.queue=[None for _ in range(size)]
        self.front=size-1
        self.rear=size-1

    def isFullQ(self):
        if (self.rear+1)%len(self.queue) == self.front:
            return True
        else: return False

    def isEmptyQ(self):
        if self.front == self.rear :
            return True
        else: return False

    def enQ(self, item):
        if self.isFullQ():
            return
        else:
            self.rear=(self.rear+1)%len(self.queue)
            self.queue[self.rear]=item
        
    def deQ(self):
        if self.isEmptyQ():
            return
        else:
            self.front=(self.front+1)%len(self.queue)
            item= self.queue[self.front]
            self.queue[self.front]=None
            return item
#원형큐 구현
t = int(input())
for i in range(t):
    size, times = map(int, input().split())
    list_ = list(map(int,input().split()))
    q=cQueue(size+1)
#큐의 크기는 들어갈 item 숫자보다 1 만큼 커야 함
    for num in list_:
        q.enQ(num)
#큐에 값들을 넣는다
    for k in range(times):
        q.enQ(q.deQ())
#큐에서 꺼네서 다시 집어넣는다.(선입후출)
    print(f'#{i+1} {q.queue[(q.front+1)%(size+1)]}')
#맨 앞에 있는 값을 꺼낸다. %size은 프론트가 큐의 마지막을 가리킬 때 맨처음으로 돌아가라는 뜻
