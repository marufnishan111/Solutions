class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=sorted(list(sentence))
        m=""
        for i in s:
            if i not in m:
                m+=i

        a="abcdefghijklmnopqrstuvwxyz"
        
        return a in m
