class Solution:
    def firstPalindrome(self, s: List[str]) -> str:
        for e in s:
            if e==e[::-1]:
                return e
        return ""