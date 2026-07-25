class Solution:
    def isHappy(self, n: int) -> bool:
        s=str(n)
        while len(s)>1:
            d=0
            for i in s:
                d+=(pow(int(i),2))
            s=str(d)
        return int(s)==1 or int(s)==7