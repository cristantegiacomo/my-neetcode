class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=collections.defaultdict(list)

        for s in strs:
            mp[str(sorted(s))].append(s)
        
        res=[ l for l in mp.values() ] #oppure: res=list(mp.values())
        return res

