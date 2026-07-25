class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=sorted(nums)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        if len(self.nums)>=self.k:
            return self.nums[-self.k] 
        else:  return 0
