from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    queue = deque()

    # Step 1). 썩은 오렌지 찾아가기
    fresh_oranges = 0
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1


    queue.append((-1, -1))

    # Step 2). BFS로 돌리기
    minutes_elapsed = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        print(queue)
        row, col = queue.popleft()
        if row == -1:
            # 한바퀴 진행 끝나고
            minutes_elapsed += 1
            if queue:  # 계속 루프를 돌릴 수 있도록 큐에 추가
                queue.append((-1, -1))
        else:
            # 썩은 오랜지
            # 주변에 있는 오랜지를 썩힐 예정
            for d in directions:
                neighbor_row, neighbor_col = row + d[0], col + d[1]
                if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                    if grid[neighbor_row][neighbor_col] == 1:
                        # 오랜지가 1이면 2로 감염시키기
                        grid[neighbor_row][neighbor_col] = 2
                        fresh_oranges -= 1
                        # 이 오렌지는 곧 다른 오렌지를 감염시킬예정
                        queue.append((neighbor_row, neighbor_col))

    # 한바퀴 돌릴때마다(4방향 다돌리고) 시간은 더해지고 신선한 오렌지가 0개가 되면 경과된 시간을 조지만 아니면 -1을 리턴
    return minutes_elapsed if fresh_oranges == 0 else -1