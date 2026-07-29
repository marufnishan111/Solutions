class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #return n>0 and not n&n-1 and not (n-1)%3
        while n>1:
            if n//4!=n/4:
                return False
            n//=4
        return n==1