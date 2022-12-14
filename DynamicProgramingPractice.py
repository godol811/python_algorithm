import sys

x = int(sys.stdin.readline().rstrip())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍 진행 (바텀업)
for i in range(2, x + 1):

    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수에서 2를 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수에서 3를 나누는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수에서 5를 나누는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    # d[i] 는 흐름을 흐르고 타서 처음엔 뺀거, 2로 나눈거, 3, 5를 나눈것 중에 최솟갑을 구하는 것이다)
print(d[x])
