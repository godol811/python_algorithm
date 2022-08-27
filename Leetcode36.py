#https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 열의 개수는 9개
        N = 9
        # 중복 확인을 위해 각 열당 set() 배열을 넣기
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):

                val = board[r][c]
                # 입력된게 없으면 그냥 continue
                if val == ".":
                    continue
                # row 안에 같은 값이 있으면 False 리턴
                if val in rows[r]:
                    return False

                # 없는값 add 해주기
                rows[r].add(val)

                # cols 안에 같은 값이 있으면 False 리턴
                if val in cols[c]:
                    return False
                # 없는값 add 해주기
                cols[c].add(val)

                # 박스 9개를 각 세션마다 구분하기
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                # 없는값 add 해주기
                boxes[idx].add(val)
        # 위의 제약 다 해결하면 Valid한 스도쿠가 되므로 TRUE 리턴
        return True



