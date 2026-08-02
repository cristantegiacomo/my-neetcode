class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        counts = Counter(s1)
        mp = collections.defaultdict(int)

        for r in range(len(s2)):   
            if s2[r] in counts and mp[s2[r]]<counts[s2[r]]:
                t = True
                mp[s2[r]]+=1
                print("mp:", mp, "\ncounts:", counts)
                for c in counts:
                    if counts[c] != mp[c]:
                        t = False
                if t:
                    return True

            elif s2[r] not in counts: 
                while l <= r:
                    if mp[s2[l]] > 0:
                        mp[s2[l]] -= 1
                    l += 1

            else:
                while mp[s2[r]]==counts[s2[r]]:
                    mp[s2[l]] -= 1
                    l += 1
                mp[s2[r]] += 1
        return False

# dcdadac


# s1 = "ab", s2 = "eidbxababoo"