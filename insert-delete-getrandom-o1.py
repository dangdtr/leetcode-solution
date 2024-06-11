import random


class RandomizedSet:

    def __init__(self):
        self.instance = {}

    def insert(self, val: int) -> bool:
        if self.instance.get(val) is None:
            self.instance[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.instance.get(val) is None:
            return False

        del self.instance[val]
        return True

    def getRandom(self) -> int:
        return random.choices(list(self.instance.keys()), k=1)[0]


randomizedSet = RandomizedSet()
randomizedSet.insert(1)  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2)  # Returns false as 2 does not exist in the set.
randomizedSet.insert(2)  # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom())   # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1)  # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2)  # 2 was already in the set, so return false.
print(randomizedSet.getRandom())  # Since 2 is the only number in the set, getRandom() will always return 2.
