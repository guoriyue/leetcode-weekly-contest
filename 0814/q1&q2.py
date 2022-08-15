class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        n = len(edges)
        score = [0 for i in range(n)]
        for i in range(n):
            score[edges[i]] += i
        idx = -1
        maxx = -1
        for i in range(n):
            if score[i] > maxx:
                maxx = score[i]
                idx = i
        return idx
      
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(grid)
        for i in range(n-2):
            temp = []
            for j in range(n-2):
                max_in_3_3 = -1
                for k in range(3):
                    for q in range(3):
                        max_in_3_3 = max(max_in_3_3, grid[i+k][j+q])
                temp.append(max_in_3_3)
            result.append(temp)
        return result
