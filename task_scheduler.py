from collections import deque
from collections import Counter
def leastInterval(tasks, n):
    q = deque(maxlen=n)
    c = Counter(tasks)
    i = 0
    interval_count = 0
    while c - Counter() != Counter(): #check if counter is empty
        next_task = c.most_common()[i][0]
        key_count = len(set(c-Counter()))
        # print(c)
        # print(q)
        # print(i)
        if next_task in q:
            if (i == key_count-1):
                q.append('')
                # print("")
                interval_count += 1
                i = 0
            else:
                i = i+1
        else:
            q.append(next_task)
            # print(next_task)
            c.subtract(next_task)
            interval_count += 1
            i = 0
    return interval_count
    




if __name__ == "__main__":
    # tasks = ["A","A","A","B","B","B"]
    tasks = ["A","A","B","C"]
    n = 2
    print(leastInterval(tasks,n))