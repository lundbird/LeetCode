import sys


def insertion_sort(A):
    B = []
    for i in range(len(A)):
        j = 0
        while (j < len(B) and B[j] < A[i]):  # need to check bounds on B
            j += 1
        B.insert(j, A[i])
    return B


def bubble_sort(A):
    for i in range(len(A)-1):
        for i in range(len(A)-1):
            if (A[i+1] < A[i]):
                A[i], A[i+1] = A[i+1], A[i]
    return A


def bucket_sort(A):
    buckets = 3
    max_val = max(A)
    B = [None] * buckets
    for i in range(buckets):
        B[i] = []

    for i in range(len(A)):
        if (A[i] >= max_val // 3 * 2):
            B[2].append(A[i])
        elif (A[i] >= max_val // 3 * 1):
            B[1].append(A[i])
        elif (A[i] >= max_val // 3 * 0):
            B[0].append(A[i])
    C = []
    for i in range(len(B)):
        B[i] = bubble_sort(B[i])
        C.extend(B[i])
    return C


def merge_sort(A):
    if len(A) <= 1:
        return A
    left = merge_sort(A[:len(A)//2])
    right = merge_sort(A[len(A)//2:])

    r_ptr, l_ptr = 0, 0
    for i in range(len(A)):
        if (r_ptr > len(right) or l_ptr < len(left) and left[l_ptr] < right[r_ptr]):
            A[i] = left[l_ptr]
            l_ptr += 1
        else:
            A[i] = right[r_ptr]
            r_ptr += 1
    return A


def quick_sort(A):
    pass


if __name__ == "__main__":
    A = [[None]*7]*6
    A_sorted = [1, 2, 3, 4, 5, 6, 7]
    A[0] = [1, 2, 3, 4, 5, 6, 7]
    A[1] = [7, 6, 5, 4, 3, 2, 1]
    A[2] = [4, 2, 6, 1, 7, 3, 5]
    A[3] = [7, 6, 5, 4, 1, 2, 3]
    A[4] = [1, 3, 5, 7, 2, 4, 6]
    A[5] = [7, 5, 6, 4, 1, 3, 2]
    for i in range(6):
        assert A_sorted == insertion_sort(A[i]), insertion_sort(A[i])
        assert A_sorted == bubble_sort(A[i]), bubble_sort(A[i])
        assert A_sorted == bucket_sort(A[i]), bucket_sort(A[i])
        assert A_sorted == merge_sort(A[i]), merge_sort(A[i])
