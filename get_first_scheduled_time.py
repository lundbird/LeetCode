def get_first_schedule(A,B,dur):
    pa, pb = 0,0
    while pa<len(A) and pb<len(B):
        start = max(A[pa][0],B[pb][0])
        end = min(A[pa][1],B[pb][1])
        if end-start >= dur:
            return [start,start+dur]
        else:
            #increment the ?earlier? schedule
            if A[pa][0] < B[pb][0]:
                pa += 1
            else:
                pb += 1
    return -1




A = [[10, 50], [60, 120], [140, 210]]
B = [[0, 15], [60, 70]]
dur = 12
print(get_first_schedule(A,B,dur))