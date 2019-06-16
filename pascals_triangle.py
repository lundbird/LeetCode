class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]*numRows
        for i in range(1,numRows):
            this_row = [1]*(i+1)
            last_row = res[i-1]
            for j in range(1,i):
                this_row[j] = last_row[j-1]+last_row[j]
            res[i] = this_row
        return res
                