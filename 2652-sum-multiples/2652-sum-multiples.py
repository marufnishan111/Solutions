class Solution:
    def sumOfMultiples(self, n: int) -> int:
        x=0
        for i in range(1,n+1):
            if not i%3 or not i%5 or not i%7:
                x+=i
        
        return x