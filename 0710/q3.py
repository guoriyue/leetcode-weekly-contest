class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
#         ls = ''
#         lt = ''
#         left_idx_start = []
#         right_idx_start = []
#         left_idx_target = []
#         right_idx_target = []
#         n = len(start)
#         flag = 0
#         for i in range(n):
#             if start[i] == 'L' or start[i] == 'R':
#                 ls = ls + start[i]
#                 if start[i] == 'L':
#                     left_idx_start.append(i)
#                     flag = 1
#                 else:
#                     right_idx_start.append(i)
#             if target[i] == 'L' or target[i] == 'R':
#                 lt = lt + target[i]
#                 if target[i] == 'L':
#                     left_idx_target.append(i)
#                 else:
#                     right_idx_target.append(i)
#                     if len(right_idx_target) > len(right_idx_start):
#                         return False
#             if flag == 1:
#                 if len(left_idx_target) < len(left_idx_start):
#                         return False
#                 flag = 0
            
#         if not (ls == lt):
#             return False
        q, av = collections.deque(), set(['L', 'R'])

        for i, c in enumerate(start):
            if c in av: q.append((i, c))

        for i, c in enumerate(target):
            if c in av:
                if not q: return False

                ind, char = q.popleft()
                if c != char: return False
                elif c == 'R' and i < ind: return False 
                elif c == 'L' and i > ind: return False 

        return not q 
        # for i in range(len(left_idx_target)):
        #     if left_idx_start[i] >= left_idx_target[i]:
        #         continue
        #     else:
        #         return False
        # for i in range(len(right_idx_target)):
        #     if right_idx_start[i] <= right_idx_target[i]:
        #         continue
        #     else:
        #         return False
        return True
        
                
