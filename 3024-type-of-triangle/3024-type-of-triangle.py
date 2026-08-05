class Solution:
    def triangleType(self, n: List[int]) -> str:

        n.sort()
        if n[0]+n[1]<=n[2]:
            return "none"
        x=len(set(n))
        if x==1:
            return "equilateral"
        elif x==2:
            return "isosceles"
        else:
            return "scalene"