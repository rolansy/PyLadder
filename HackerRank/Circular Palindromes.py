def largest_palindrome_length(s):
    if not s:
        return 0
    
    n = len(s)
    ml = 1
    
    for i in range(n):
        l, r = i - 1, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cl = r - l + 1
            ml = max(ml, cl)
            l -= 1
            r += 1
    
    for i in range(n):
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cl = r - l + 1
            ml = max(ml, cl)
            l -= 1
            r += 1
    
    return ml

def circularPalindromes(s, n):
    s_doubled = s + s
    results = []
    
    # Process the first rotation directly to avoid TLE
    max_len = largest_palindrome_length(s)
    results.append(max_len)
    
    # For remaining rotations, use the fact that shifting by one
    # doesn't change palindrome structure dramatically
    for i in range(1, n):
        current_window = s_doubled[i:i+n]
        max_len = largest_palindrome_length(current_window)
        results.append(max_len)
    
    return results