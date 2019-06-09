def two_sum(A,target):
    l,r = 0 ,len(A)-1
    A.sort()
    while l<r:
        sum = A[l]+A[r]
        if sum == target:
            return True
        elif sum < target:
            l += 1
        else:
            r -= 1
    return False


A=[2, 7, 11, 15]
target = 9
print(two_sum(A,target))
