class Solution:
    def reverse(self, x: int) -> int:
        m=str(x)[::-1]
        if x<0:
            m=-1*int(m[:-1])
            if m<(-pow(2,31)):
                return 0
            return m
        else:
            m=int(m)
            if m>(pow(2,31)-1):
                return 0
            return int(m)
        