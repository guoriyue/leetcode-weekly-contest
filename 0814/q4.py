import math
from scipy.special import comb, perm 
from itertools import  permutations
class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
#         # 2 9
#         # 3 19 101  121 131 141 151 161 171 181 191          110 111 112 113 114 115 116 117 118 119 
#         # 9 * 19 = 171
#         # 4 1 2  (100 + 9*(10+9)) * 9
#         # 120
#         # (10 + 9*1 ) * 9
#         items = [1, 9]
#         single = [1]
#         e = 10
#         while len(items) < 10:
#             items.append((e + 9 * single[-1])*9)
#             single.append(e + 9 * single[-1])
#             e=e*10
#         # print(items)
#         # print(single)
#         x = len(str(n))
#         if x == 1:
#             return 0
#         elif x == 2:
#             if n == 10:
#                 return 0
#             else:
#                 if str(n)[1] >= str(n)[0]:
#                     return int(str(n)[0])
#                 else:
#                     return int(str(n)[0]) - 1
                
#         s = str(n)
#         idx = len(s)
#         ret = items[idx-2]
        
#         for k in s:
#             b = int(k) - 1
#             ret = ret + items[idx - 2] * b
#             idx -= 1
#             if idx == 2:
#                 break
                
#         x = len(str(n)[-2:])
#         p = str(n)[-2:]
#         if x == 1:
#             ret += 0
#         elif x == 2:
#             if int(p) == 10:
#                 ret += 0
#             else:
#                 if p[1] >= p[0]:
#                     ret += int(p[0])
#                 else:
#                     ret += int(p[0]) - 1
#         return ret

        nums = [int(i) for i in str(n+1)] # digits in n+1
        d = len(nums) # number of digits in n+1
        res = 0 # number of no duplicates
        
        # count no duplicates for numbers with <d digits
        for i in range(1,d):
            # for j in permutations(9,i-1):
            #     print(j)
            
            res += 9 * perm(9,i-1)
        
		# count no duplicates for numbers with d digits and smaller than n
        for i, x in enumerate(nums):
            if i == 0:
                digit_range = range(1,x) # first digit can not be 0
            else:
                digit_range = range(x)
                
            for y in digit_range:
                if y not in nums[:i]:
                    res += perm(9-i,d-1-i)
            if x in nums[:i]: break
                
        return int(res)
        
