class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        x,y=1,0
        for i in n:
            i=int(i)
            x*=i
            y+=i
        return x-y