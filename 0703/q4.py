class Solution(object):
    def __init__(self):
        self.record=[]
        self.dx=[1,-1,0,0]
        self.dy=[0,0,1,-1]
        self.mod=1000000007
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m=len(grid)
        n=len(grid[0])
        # record=[]
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(-1)
            self.record.append(t)
            

        for i in range(m):
            for j in range(n):
                if self.record[i][j]==-1:
                    self.dfs(i,j,m,n,grid)
        # print(self.record)
        final=0
        for i in range(m):
            for j in range(n):
                final=final+self.record[i][j]
                final%=self.mod
        return final
    
    def dfs(self, i, j, m, n, grid):
        x=0
        success=0
        for k in range(4):
            di=i+self.dx[k]
            dj=j+self.dy[k]
            if di>=0 and di<m and dj>=0 and dj<n:
                if grid[i][j]>grid[di][dj]:
                    success+=1
                    if not self.record[di][dj]==-1:
                        x=x+self.record[di][dj]
                        x%=self.mod
                    else:
                        self.dfs(di,dj,m,n,grid)
                        x=x+self.record[di][dj]
                        x%=self.mod
        if success==0:
            self.record[i][j]=1
        else:
            self.record[i][j]=x+1
        return x
            
        
        
