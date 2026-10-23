class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm=defaultdict(list)
        from collections import Counter
        for s in strs:
            asc=str(sorted(s))
            if asc in hm:
                hm[asc].append(s)
            else:
                hm[asc].append(s)
        
        return list(hm.values())


        