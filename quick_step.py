from collections import deque
def quick_step(n):
    counts = deque([1,1,2],maxlen=3)
    for i in range(2,n):
        counts.append(counts[0]+counts[1]+counts[2])
    return counts.pop()

if __name__ == "__main__":
    print(quick_step(3))
    print(quick_step(4))
    print(quick_step(5))
    print(quick_step(6))
