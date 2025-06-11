def sherlockAndAnagrams(s):
    from collections import defaultdict
    count = defaultdict(int)
    n = len(s)
    for length in range(1, n):
        for i in range(n - length + 1):
            sub = s[i:i+length]
            key = tuple(sorted(sub))
            count[key] += 1
    res = 0
    for v in count.values():
        res += v * (v - 1) // 2
    return res