# 최초의 개수 가져오기
n = int(input())
# 튜플 배열 설정하기
arr = []

for i in range(n):
    # 무조건 int로 map 해서 받아올것
    x, y = map(int, input().split())
    arr.append((x, y))

# 람다나 소팅 이나 일단 같다.
arr.sort(key= lambda x: (x[0], x[1]))
arr.sort()

# 출력하기
for e in arr:
    print(e[0], e[1])
