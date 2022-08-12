import sys
#  출력전 런타임에러를 막기 위해 limit을 정해둠

sys.setrecursionlimit(10**6) #10의 6승

#  DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):

    if x <= -1 or x > m-1 or y <= -1 or y > n-1:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        # 상하좌우 대각선 의 위치도 모두 재귀적으로 호출  8방향
        dfs(x + 1, y)  # 6
        dfs(x + 1, y + 1)  # 5
        dfs(x + 1, y - 1)  # 7
        dfs(x - 1, y + 1)  # 2
        dfs(x - 1, y - 1)  # 10
        dfs(x - 1, y)  # 12

        dfs(x, y - 1)  # 9
        dfs(x, y + 1)  # 3
        # dfs(x, y)
        return True
    return False


while True:
    # n,m을 공백으로 구분하여 입력받기
    n, m = map(int, input().split())

    if not n and not m:
        break

    # 2차원 리스트의 맵 정보 입력받기
    graph = [list(map(int, input().split())) for _ in range(m)]

    count = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                count += 1

    print(count)
