from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        q=deque()
        m=len(mat)
        n=len(mat[0])
        dist=[[-1]*n for k in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    dist[i][j]=0
                    q.append((i,j))
        while q:
            r,c=q.popleft()
            # UP
            if r-1>=0 and dist[r-1][c]==-1:
                dist[r-1][c]=dist[r][c]+1
                q.append((r-1,c))
                                
            # DOWN
            if r+1<m and dist[r+1][c]==-1:
                dist[r+1][c]=dist[r][c]+1
                q.append((r+1,c))

            # LEFT
            if c-1>=0 and dist[r][c-1]==-1:
                dist[r][c-1]=dist[r][c]+1
                q.append((r,c-1))

            # RIGHT
            if c+1<n and dist[r][c+1]==-1:
                dist[r][c+1]=dist[r][c]+1
                q.append((r,c+1))
        return dist