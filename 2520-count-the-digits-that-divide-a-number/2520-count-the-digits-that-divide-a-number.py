class Solution:
    def countDigits(self, n: int) -> int:
        s=str(n)
        m=0
        for i in s:
            if not n%(int(i)):
                m+=1
        return m