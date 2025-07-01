class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        a=0
        b=0
        n=len(s)
        m=len(t)
        while b<m:
            if s[a]==t[b]:
                a+=1
                b+=1
            else:
                b+=1
            if a==n:
                return True
        return False