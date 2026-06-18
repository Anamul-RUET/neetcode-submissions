class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for s in strs:
            tmp=''.join(sorted(s))
            mp[tmp].append(s)
        return list(mp.values())