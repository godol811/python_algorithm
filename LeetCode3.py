# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = Counter()
        left = right = 0

        res = 0

        while right < len(s):
            print(left, right, chars)
            r = s[right]
            chars[r] += 1
            # chars[r] 하나 더했는데 만약 2개가 되면 반복 되는 것이므로 앞에서 있는 리스트들을 하나씩 올리기
            # left가 하나씩 올라가서 char[r]을 1로 줄여주기
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            # 반복되는 단어 사이에서 최대의 간격을 찾기 MAX 함수
            res = max(res, right - left + 1)
            # 오른쪽으로 옮기기 (Sliding)
            right += 1
        return res