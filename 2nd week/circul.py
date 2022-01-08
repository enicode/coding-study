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
t = int(input())
for i in range(t):
    size, times = map(int, input().split())
    list_ = list(map(int,input().split()))
    q=cQueue(size+1)
    for num in list_:
        q.enQ(num)
    for k in range(times):
        q.enQ(q.deQ())
    print(f'#{i+1} {q.queue[(q.front+1)%(size+1)]}')