import sys

n, m = map(int, (sys.stdin.readline().rstrip().split()))
riceCakes = list(map(int, sys.stdin.readline().rstrip().split()))
riceCakes.sort()


# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(riceCakes)

# 이진탐색 수행 (반복적)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    # 다 짜르고 남은거 합치는 작업
    for x in riceCakes:
        if x > mid:
            total += x - mid

    # 만약 남은거 합친게 목표치 보다 작으면 좀더 짜르기
    if total < m:
        end = mid - 1

    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result를 기록
        start = mid + 1
print(result)
