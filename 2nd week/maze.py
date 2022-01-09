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
#stack 구현
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
# 다음 가려는 길이 막혔거나 미로 바깥이면 True 반환 아니면 False 반환 하는 함수, 0:상, 1:우, 2:좌, else:하
def isBackword(x,y,path):
    for i in range(path.top+1):
        if path.stack[i][0]==x and path.stack[i][1]==y:
            return True
    return False
# 다음에 가려는 길이 이미 지나온길에 포함되면 True 반환 아니면 False 반환

t = int(input())
for _ in range(t):
    size=int(input())
    maze = [None for _ in range(size)]
    for i in range(size, 0,-1):
        string_=input()
        for k in range(size):
            if string_[k] == '2':
                origin=[k,i-1] # 2인 곳이 출발지점
            elif string_[k] == '3':
                exit=[k,i-1] # 3인 곳은 출구
        maze[i-1]=string_  
    path = sTack(size**2) # 아무리 경로가 길어도 미로 면적보다 클순없으므로
    path.push(origin) # 처음 좌표를 스택에 저장
    can=0 # 가능한지 알려주는 값 가능하면 1, 불가능하면 0
    while True:
        x = path.peek()[0]
        y = path.peek()[1]
        # 탐색을 시작할 좌표
        if ([x+1,y]==exit) or ([x-1,y])==exit or ([x,y+1])==exit or ([x,y-1])==exit:
            can=1
            break
        # 만약 상 하 좌 우 어느 한 곳에 출구가 존재하면 can=1 바꾸고 탈출
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
        # while 문에 처음들왔을 때만 쓰는 함수, 
        elif isClosed(path.peek(),maze,0) or isBackword(x,y+1,path): # 위가 막혔거나 이미 왔던 곳이면
            if isClosed(path.peek(),maze,1) or isBackword(x+1,y,path): # 오른쪽이 막혔거나 이미 왔던 곳이면
                if isClosed(path.peek(),maze,2) or isBackword(x-1,y,path): # 왼쪽이 막혔거나 이미 왔던 곳이면
                    if isClosed(path.peek(),maze,3) or isBackword(x,y-1,path): # 아래쪽이 막혔거나 이미 왔던 곳이면
                        line=maze[y][:x]+'1'+maze[y][x+1:]
                        maze[y]=line
                        path.pop()
                        tmp=path.pop()
                        back=path.peek()
                        path.push(tmp)
                        # 사방이 막혔으므로 그 자리를 1로 매워버리고 경로를 하나 거슬러간다.
                    else:
                        path.push([x,y-1]) # 아래로 간다.
                else: 
                    path.push([x-1,y]) # 왼쪽으로 간다.
            else: 
                path.push([x+1,y]) # 오른쪽으로 간다.
        else: 
            path.push([x,y+1]) # 위로 간다.

    print(f'#{_+1} {can}')