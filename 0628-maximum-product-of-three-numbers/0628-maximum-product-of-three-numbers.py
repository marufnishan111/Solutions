class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        m=sorted(n,key=abs)
        x=sorted(n)
        return max(m[-1]*m[-2]*m[-3],m[-1]*m[0]*m[-2],x[-1]*x[-2]*x[-3],x[0]*x[1]*x[-1])
