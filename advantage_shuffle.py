class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        #for each value in B, find the smallest value in A greater than it
        #if no value in A > then B[i], match with smallest remaining value of A
        #note when deleting items from array, consider iterating in reverse so you always take the last most element anyway and its just a pop
        A.sort()
        res = [None]*len(B)
        for i,val in enumerate(B):
            index = bisect.bisect_right(A,val)
            if index == len(A):
                min_a = min(A)
                res[i] = min_a
                A.remove(min_a)
            else:
                res[i] = A[index]
                A.pop(index)
        return res