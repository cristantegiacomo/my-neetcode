class Solution:
    def tribonacci(self, n: int) -> int:
      mp = defaultdict(int)

      mp[0] = 0
      mp[1] = 1
      mp[2] = 1 #1+1
      for i in range(3, n+1):
        mp[i] = mp[i-1] + mp[i-2] + mp[i-3]
      return mp[n]