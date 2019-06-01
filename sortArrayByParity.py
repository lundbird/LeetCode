class Solution(object):
    #also can use A.sort(key = lambda x: x % 2)
    def sortArrayByParity(self, A):
        even_ptr, odd_ptr = len(A)-1, 0
        while even_ptr > odd_ptr:
            if A[even_ptr] % 2 != 0:
                even_ptr -= 1
                continue #trick is to do one increment/decrement per operation so while loop condition works
            if A[odd_ptr] % 2 != 1:
                odd_ptr += 1
                continue
            A[even_ptr], A[odd_ptr] = A[odd_ptr], A[even_ptr]
            even_ptr -=1
            odd_ptr +=1
        return A