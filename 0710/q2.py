class SmallestInfiniteSet(object):

    def __init__(self):
        self.set = [i for i in range(1, 1005)]

    def popSmallest(self):
        """
        :rtype: int
        """
        ret = self.set[0]
        self.set = self.set[1:]
        return ret

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.set:
            return None
        self.set.append(num)
        self.set.sort()
        return None
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
