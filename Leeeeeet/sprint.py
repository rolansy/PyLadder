def minimumLength( s):
        """
        :type s: str
        :rtype: int
        """
        while True:
            if s=="":
                return 0
            x=s[0]
            if s.lstrip(x)!=s and s.rstrip(x)!=s:
                s=s.strip(x)
                continue
            else:
                return len(s)
        
        
s="ca"
print(minimumLength(s))