class Solution:
    def tribonacci(self, n: int) -> int:
      Tr = defaultdict(int)

      Tr[0] = 0
      Tr[1] = 1
      Tr[2] = 1
      for i in range(3, n+1):
        Tr[i] = Tr[i-1] + Tr[i-2] + Tr[i-3]
      return Tr[n]