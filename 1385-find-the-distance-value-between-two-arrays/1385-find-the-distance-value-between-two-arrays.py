class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        m=0
        for i in a:
            x=1
            for j in b:
                if abs(i-j)<=d:
                    x=0
                    break
            if x:
                m+=1
        return m