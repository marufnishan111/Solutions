class Solution:
    def minimumSum(self, num: int) -> int:
        x=[int(i) for i in str(num)]

        x.sort()
        x[1],x[2]=x[2],x[1]



        return x[0]*10+x[1]+x[2]*10+x[3]