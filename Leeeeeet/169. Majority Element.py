def majorityElement(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    m=0
    for k,v in d.items():
        if v>m:
            mx=k
            m=v
    return mx