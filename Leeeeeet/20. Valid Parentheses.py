
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in mp:
                st.append(c)
            else:
                if not st or st.pop() != mp[c]:
                    return False

        return len(st) == 0
        