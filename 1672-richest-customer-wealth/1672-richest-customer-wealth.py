class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        m=[]
        for i in a:
            m.append(sum(i))
        return max(m)