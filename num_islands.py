 class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(r,c):
            #add all island squares to the visited set
            q = collections.deque([(r,c)])
            while q:
                cr,cc = q.popleft()
                grid[cr][cc] = "0"
                for next_r,next_c in [(cr-1,cc),(cr,cc-1),(cr+1,cc),(cr,cc+1)]:
                    if 0<=next_r<len(grid) and 0<=next_c<len(grid[0]) and grid[next_r][next_c]=="1":
                        q.append((next_r,next_c))
            
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    islands += 1
                    bfs(r,c)
        return islands 
                        
                
            