# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        matrix=[]
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(-1)
            matrix.append(t)
                
        p=head
        vals=[]
        while p:
            v=p.val
            vals.append(v)
            p=p.next
        left=0
        right=n-1
        top=0
        bottom=m-1
        cnt=0
        try:
            while left<=right and top<=right:
                for col in range(left,right+1):
                    matrix[top][col]=vals[cnt]
                    cnt+=1

                for row in range(top+1,bottom+1):
                    matrix[row][right]=vals[cnt]
                    cnt+=1
                if left<right and top<bottom:
                    for col in range(right-1,left,-1):
                        matrix[bottom][col]=vals[cnt]
                        cnt+=1
                    for row in range(bottom,top,-1):
                        matrix[row][left]=vals[cnt]
                        cnt+=1
                left+=1
                right-=1
                top+=1
                bottom-=1
        except Exception as e:
            pass
        return matrix
 

