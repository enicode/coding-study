def solution(routes):
    routes.sort(key=lambda x:(x[1],x[0]))
    answer = 0
    while len(routes) != 0:
        camera=routes[0][1]
        answer += 1
        while len(routes) != 0:
            if camera in range(routes[0][0],routes[0][1]+1):
                del routes[0]
            else: break
    return answer


    ## 1. 들어온 모든 루트를 나간 지점을 기준으로 오름차순 정렬한다 만약에 나간 지점이 같다면 들어온 지점을 기준으로 오름차순으로 정렬한다.
    ## 2. 그렇게 정렬된 처음 루트의 나간 지점에 카메라를 설치한다.
    ## 3. 카메라를 설치 횟수를 1증가 시킨다.
    ## 4. 나간지점을 포함하는 모든 루트들을 삭제한다.
    ## 5. 남은 루트들 중에 제일 나가는 지점이 빠른 루트의 나간지점에 카메라를 설치한다.
    ## 2~4 반복
    ## 남은 루트가 없을경우 카메라 설치 횟수를 리턴한다.

routes=[[-20,-15],[-14,-5],[-18,-13],[-5,-3],[-5,-2],[-4,1],[-4,-3]]
num_camera=solution(routes)
print(num_camera)

