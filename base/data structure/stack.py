import sys

input=sys.stdin.readline

class Stack():
    def __init__(self,n):
        self.stack = [None for _ in range(n)]
        self.s_top = -1

    def push(self, item):
        self.s_top += 1
        self.stack[self.s_top]=item   
        return

    def pop(self):
        if self.empty()==1:
            return -1
        else:
            tmp = self.stack[self.s_top]
            self.stack[self.s_top] = None
            self.s_top -= 1         
            return tmp

    def size(self):
        return self.s_top + 1

    def empty(self):
        if self.s_top == -1:
            return 1
        else:
            return 0
    def stack_top(self):
        if self.empty()==1:
            return -1
        else: 
            return self.stack[self.s_top]
#문제에서 요구한 스택 구현
n = int(input())
stack=Stack(n)
for _ in range(n):
    com = input().strip()
    if com == 'pop':
        print(stack.pop())
    elif com == 'size':
        print(stack.size())
    elif com =='empty':
        print(stack.empty())
    elif com == 'top':
        print(stack.stack_top())
    else:
        x = int(com[5:])
        stack.push(x)