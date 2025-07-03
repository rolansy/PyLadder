class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            ix="".join(sorted(i))
            if ix not in list(h.keys()):
                h[ix]=[i]
            else:
                h[ix].append(i)
        return list(h.values())      