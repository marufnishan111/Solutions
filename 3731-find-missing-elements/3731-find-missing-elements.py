class Solution:
    def findMissingElements(self, n: List[int]) -> List[int]:
        m=[]
        for i in range(min(n),max(n)+1):
            if i not in n:
                m.append(i)

        return m