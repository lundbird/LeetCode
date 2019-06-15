def binary_search(A,val) -> int:
    l,r = 0, len(A)
    while l<r:
        m = (l+r)//2 #m will never equal r here so r must start at len(A) not len(A)-1
        if A[m] is None:
            r -= 1
            continue
        if val == A[m]:
            return m
        elif val < A[m]:
            r = m
        else:
            l = m + 1 #increase by one or else we can get infinite loop where m doesn't move

def binary_search_lowest_duplicate(A,val) -> int:
    l,r = 0, len(A)
    while l<r:
        m = (l+r)//2 #m will never equal r here so r must start at len(A) not len(A)-1
        if val == A[m]:
            if m==0 or A[m-1]!=val:
                return m
            else:
                r = m
        elif val < A[m]:
            r = m
        elif val > A[m]:
            l = m + 1 #increase by one or else we can get infinite loop where m doesn't move
        else:
            #handle None in Array by moving m to the next lower non None entry
            r -= 1
    

A = [0,1,2,3,4,5]
print(binary_search(A,-1))
print(binary_search(A,0))
print(binary_search(A,.5))
print(binary_search(A,1))
print(binary_search(A,2))
print(binary_search(A,3))
print(binary_search(A,4))
print(binary_search(A,5))
print(binary_search(A,6))

print(binary_search([None,None,None],0))
print(binary_search([0,None,None],0))
print(binary_search([None,None,2],2))




A = [0,1,1,1,2,3,4]
print(binary_search_lowest_duplicate([0,1,1,1,2,3,4],1)) #1
print(binary_search_lowest_duplicate([0,0,0,2,3,4],0)) #0
print(binary_search_lowest_duplicate([0,0,0,3,4,4],4)) #4






