class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=set(list(s))
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return -1