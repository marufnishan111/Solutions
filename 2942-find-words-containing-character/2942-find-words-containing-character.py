class Solution:
    def findWordsContaining(self, s: List[str], x: str) -> List[int]:
        m=[]
        for i in range(len(s)):
            if x in s[i]:
                m.append(i)
        return m