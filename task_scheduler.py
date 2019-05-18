from collections import deque
from collections import Counter
from collections import OrderedDict
def leastInterval(tasks, n):
    q = deque(maxlen=n)
    c = Counter(tasks).most_common()
    i = 0
    interval_count = 0
    while len(c) != 0: #check if counter is empty
        print(c)
        next_task = c[i][0]
        if next_task in q:
            if (i == len(c)-1):
                q.append('')
                interval_count += 1
                i = 0
            else:
                i = i+1
        else:
            q.append(next_task)
            c[i] = (c[i][0],c[i][1]-1)
            if c[i][1] == 0:
                del(c[i])
            interval_count += 1
            i = 0
    return interval_count
    




if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    # tasks = ["A","A","B","C"]
    n = 2
    print(leastInterval(tasks,n))