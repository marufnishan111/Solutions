class Solution:
    def xorOperation(self, n: int, s: int) -> int:
        m=[]
        for i in range(n):
            m.append(s)
            s+=2
        
        x=m[0]
        for i in range(1,n):
            x^=m[i]
        
        return x