'''def hillvalley(l):
  #  for i in range(len(l)):
   #     if l[i]<l[i+1]:
    i=0
    while(i<len(l)):
        if i==len(l)-1:
            return False
        if  (l[i]<l[i+1]):
            while(l[i]<l[i+1]):
                
                i+=1
            if (l[i]>l[i+1]):
                return True
        else:
            while(l[i]>l[i+1]):
                
                i+=1
            if (l[i]<l[i+1]):
                return True
            
        return False'''
'''def hillvalley(l):
    if len(l) < 3: 
        return False

    if l[1] > l[0]:  
        ascending = True
    else:  
        ascending = False

    for i in range(1, len(l) - 1):
        if ascending:
            if l[i] > l[i+1]:  
                ascending = False
        else: 
            if l[i] < l[i+1]:  
                return False

    return not ascending
'''
def hillvalley(l):
    if len(l) < 3:  # A hill or valley must have at least 3 elements
        return False

    # Determine if we start ascending or descending
    if l[1] > l[0]:  # We start ascending
        ascending = True
    else:  # We start descending
        ascending = False

    for i in range(1, len(l) - 1):
        if ascending:
            if l[i] > l[i+1]:  # Switch from ascending to descending
                ascending = False
        else:  # We are descending
            if l[i] < l[i+1]:  # If we switch back to ascending, it's not a hill or valley
                return False

    # If we've gone through the whole list without returning, it's a hill or valley
    return not ascending
print(hillvalley([1,2,3,4,5]))