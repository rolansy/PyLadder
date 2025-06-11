#User function Template for python3

class Solution:
    def findString(self, N, K):
        # De Bruijn sequence construction using DFS
        alphabet = [str(i) for i in range(K)]
        seen = set()
        ans = []

        def dfs(node):
            for x in alphabet:
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)
        
        start = "0" * (N - 1)
        dfs(start)
        return start + ''.join(ans[::-1])