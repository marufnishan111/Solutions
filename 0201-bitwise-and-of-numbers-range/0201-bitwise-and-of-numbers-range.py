class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        x=0
        while l!=r:
            l>>=1
            r>>=1
            x+=1
        return l<<x