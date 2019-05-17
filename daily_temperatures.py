def dailyTemperatures(T):
    #brute force
    result = []
    for i in range(len(T)):
        day_count = 0
        for j in range(i,len(T)):
            if T[j] > T[i]:
                result.append(day_count)
                break
            if j == len(T)-1:
                result.append(0)
            day_count += 1
    return result

def dailyTemperatures2(T):
    result = []
    for i in range(len(T)):
        greater_indices = []
        for j in range(T[i]+1,100):
            try:
                greater_indices.append(T.index(j,i)-i)
            except ValueError:
                pass
        if not greater_indices:
            result.append(0)
        else:
            result.append(min(greater_indices))
    return result

def dailyTemperatures3(T):
    stack = []
    ans = [0]*len(T)
    for i in range(len(T)-1,-1,-1):
        while stack and T[i] >= T[stack[-1]]:
            #remove all entries from stack that are less than this
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i #stack[-1] always contains next largest value
        stack.append(i)
    return ans

if __name__=="__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(T))
    print(dailyTemperatures3(T))