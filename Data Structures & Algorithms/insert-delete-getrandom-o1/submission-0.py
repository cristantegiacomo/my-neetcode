class RandomizedSet:

    def __init__(self):
        self.time_val = {}    # time -> val
        self.time = 0
        self.val_time = {}  # val -> time

    def insert(self, val: int) -> bool:
        self.time += 1
        if val not in self.val_time:
            self.val_time[val] = self.time
            self.time_val[self.time] = val
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.val_time:
            tm = self.val_time[val]
            del self.val_time[val]
            del self.time_val[tm]
            return True
        else:
            return False

    def getRandom(self) -> int:
        r = random.randint(1, self.time)
        while r not in self.time_val:
            r = random.randint(1, self.time)
        return self.time_val[r]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()