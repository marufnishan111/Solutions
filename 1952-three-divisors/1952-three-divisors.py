class Solution:
    def isThree(self, n: int) -> bool:
        i,m=1,0
        while i<=n:
            if not n%i:
                m+=1
            if m>3:
                break
            i+=1
        return m==3