def repfree(s):
    d={}
    for i in s:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    for i in list(d.values()):
        if i>1:
            return False
    return True
print(repfree("(7)(a"))