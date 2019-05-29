from collections import defaultdict
def find_val(seq, num, den):
    dict = defaultdict(list)
    for l1,l2,val in seq:
        dict[l1].append((l2,val))
        dict[l2].append((l1,val))
    print(dict)
    return dfs(num,den,dict,set())

def dfs(num,den,dict,visited):
    print(num,den,dict,visited)
    if num == den: return 1 #for recursion always put base case in front.
    visited.add(num)
    for entry in dict[num]:
        if entry[0] in visited: #best to do it like this to reduce nesting
            continue
        return dfs(entry[0],den,dict,visited) * entry[1]





test = [('a','b',3),('b','c',2.5),('c','d',4)]
print(find_val(test,'a','d'))