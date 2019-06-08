class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#       return all(r==0 or c==0 or matrix[r-1][c-1]==val for r, row in enumerate(matrix) for c, val in enumerate(row))
        n_row = len(matrix)
        n_col = len(matrix[0])
        diags = []
        res = []
        for r in range(n_row):
            diags.append((r,0))
        for c in range(1,n_col):
            diags.append((0,c))
        # print(diags)
        for start_row,start_col in diags:
            this_diag = []
            r, c = start_row, start_col
            while r<n_row and c<n_col:
                this_diag.append(matrix[r][c])
                r += 1
                c += 1
            res.append(this_diag)
        
        #check that each row has only one val
        is_same_value = [len(set(res[i]))==1 for i in range(len(res))]
        # print(res,is_same_value)
        return all(is_same_value)