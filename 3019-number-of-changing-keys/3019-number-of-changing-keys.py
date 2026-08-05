class Solution:
    def countKeyChanges(self, s: str) -> int:
        #return (len(set(list(s.lower())))-1)
        s=s.lower()
        m=0

        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                m+=1
        return m