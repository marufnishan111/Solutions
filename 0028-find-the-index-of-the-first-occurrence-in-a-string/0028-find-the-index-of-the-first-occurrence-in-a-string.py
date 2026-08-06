class Solution:
    def strStr(self, h: str, n: str) -> int:
        if n not in h:
            return -1
        else:
            return h.index(n)