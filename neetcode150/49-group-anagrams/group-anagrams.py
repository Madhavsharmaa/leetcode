class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm=defaultdict(list)
        for s in strs:
            asc=str(sorted(s))
            hm[asc].append(s)

        return list(hm.values())


        