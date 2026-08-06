class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(10):
            x=str(n)
            m=1
            for a in x:
                m*=int(a)
            if not m%t:
                return n
            else:
                n+=1