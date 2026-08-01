class Solution:
    def numberOfEmployeesWhoMetTarget(self, h: List[int], t: int) -> int:
        m=0
        for i in h:
            if i>=t:
                m+=1
        return m