class sTack():
    def __init__(self,size):
        self.stack=[None for _ in range(size)]
        self.top=-1

    def isStackFull(self) :
        if (self.top >= len(self.stack)-1) :
            return True
        else :
            return False

    def isStackEmpty(self) :
        if (self.top == -1) :
            return True
        else :
            return False

    def push(self, data) :
        if (self.isStackFull()) :
            return False
        self.top += 1
        self.stack[self.top] = [data[0],data[1]]

    def pop(self) :
        if (self.isStackEmpty()) :
            return None
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self) :
        if (self.isStackEmpty()) :
            return None
        return self.stack[self.top]

def isClosed(way,maze,dir):
    x = way[0]
    y = way[1]
    if dir == 0 :
        if y+1 <= len(maze)-1:
            if maze[y+1][x] == '1' :
                return True
            else: return False
        else: return True
    elif dir == 1 :
        if x+1 <= len(maze)-1:
            if maze[y][x+1] == '1' :
                return True
            else: return False
        else: return True
    elif dir == 2: 
        if x-1 >= 0:
            if maze[y][x-1] == '1' :
                return True
            else: return False
        else: return True
    else : 
        if y-1 >= 0:
            if maze[y-1][x] == '1' :
                return True
            else: return False
        else: return True
def isBackword(x,y,path):
    for i in range(path.top+1):
        if path.stack[i][0]==x and path.stack[i][1]==y:
            return True
    return False
#import sys
#sys.stdin = open("C:\\Users\\DongHyuk\\coding_study\\coding-study\\2nd week\\sample_input.txt", "r")
#T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
#for test_case in range(1, T + 1):

t = int(input())
for _ in range(t):
    size=int(input())
    maze = [None for _ in range(size)]
    for i in range(size, 0,-1):
        string_=input()
        for k in range(size):
            if string_[k] == '2':
                origin=[k,i-1]
            elif string_[k] == '3':
                exit=[k,i-1]
        maze[i-1]=string_  
    path = sTack(size**2)
    path.push(origin)
    can=0
    while True:
        x = path.peek()[0]
        y = path.peek()[1]
        if ([x+1,y]==exit) or ([x-1,y])==exit or ([x,y+1])==exit or ([x,y-1])==exit:
            can=1
            break
        if path.peek()==origin:
            if isClosed(path.peek(),maze,0):
                if isClosed(path.peek(),maze,1):
                    if isClosed(path.peek(),maze,2):
                        if isClosed(path.peek(),maze,3):
                            break
                        else:
                            path.push([x,y-1])
                    else: 
                        path.push([x-1,y])
                else: 
                    path.push([x+1,y])
            else: 
                path.push([x,y+1])

        elif isClosed(path.peek(),maze,0) or isBackword(x,y+1,path):
            if isClosed(path.peek(),maze,1) or isBackword(x+1,y,path):
                if isClosed(path.peek(),maze,2) or isBackword(x-1,y,path):
                    if isClosed(path.peek(),maze,3) or isBackword(x,y-1,path):
                        line=maze[y][:x]+'1'+maze[y][x+1:]
                        maze[y]=line
                        path.pop()
                        tmp=path.pop()
                        back=path.peek()
                        path.push(tmp)
                    else:
                        path.push([x,y-1])
                else: 
                    path.push([x-1,y])
            else: 
                path.push([x+1,y])
        else: 
            path.push([x,y+1])
        for i in range(size):
            print(maze[i])

    print(f'#{_+1} {can}')