import math
class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        amount.sort()
        if amount[0] + amount[1] <= amount[2]:
            return int(amount[2])
        else:
            
            delta = amount[0] + amount[1] - amount[2]
            return int(amount[2] + math.ceil(delta/2.0))
        
        
