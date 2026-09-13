from math import gcd
class Solution:
    def findGCD(self, n: List[int]) -> int:
        return gcd(min(n),max(n))
        