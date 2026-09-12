class RandomizedSet:

    def __init__(self):
        self.mp = {}    # val -> idx
        self.nums = []  # nums[idx] = val

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.mp[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        idx = self.mp[val]
        last = self.nums[-1]
        # salvo last nella posizione che voglio
        self.nums[idx] = last
        self.mp[last] = idx
        # ora l'indice di val punta a last
        self.nums.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()