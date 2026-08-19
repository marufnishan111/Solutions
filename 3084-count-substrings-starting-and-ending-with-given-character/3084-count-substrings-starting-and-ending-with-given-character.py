class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        a=s.count(c)
        return a*(a+1)//2