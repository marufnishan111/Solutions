class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        m=-float('inf')
        for i in s:
            i=i.split()
            m=max(m,len(i))
        return m