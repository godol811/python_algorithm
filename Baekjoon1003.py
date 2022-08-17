import sys

# 몇개의 숫자를 받아 올지 정하기
n = int(sys.stdin.readline().rstrip())

# n 개 만큼 반복문
for i in range(n):

    # m 열의 피보나치를 계산할것
    m = int(sys.stdin.readline().rstrip())
    #  초기 0일때 , 1일때 , 2일때 출력 수를 파악
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if m >= 3:
        for i in range(3, m + 1):
            # 그 뒤로 각자 피보나치가 형성이 됨 (zero, one)
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[m], one[m])
