class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_ordinate=[]
        map={}
        l=[]
        for st in strs:
            strs_ordinate.append("".join(sorted(st)) )
        for i, s in enumerate(strs_ordinate):
            if s not in map: map[s]=[strs[i]]
            else: map[s].append(strs[i])
        for m in map:
            l.append(map[m])
        return l
