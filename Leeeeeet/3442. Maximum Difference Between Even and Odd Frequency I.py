
def maxDifference(s):
    d={'e':float('inf'),'o':float('-inf')}
    l=[]
    for i in s:
        if i not in l:
            sc=s.count(i)
            if sc %2==0:
                d['e']=min(d['e'],sc)
            else:
                d['o']=max(d['o'],sc)
            l.append(i)
    return d['o']-d['e']