class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                        perim += 1   
                    elif grid[r][c]==0:
                        perim += 1
        return perim