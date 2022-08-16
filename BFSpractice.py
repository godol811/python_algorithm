from collections import deque

#  N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트 맴 정보 입력받기
maze = []

for i in range(maze):
    maze.append(list(map(int, input())))

# 이동할 네 방향 정의 (상,하,좌,우)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스 코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 4방향을 검색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문 하는 경우 에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
        # 가장 오른쪽 아래 까지의 최단 거리 반환
    return maze[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
