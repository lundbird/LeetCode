def find_duplicates(arr1,arr2):
  '''
  input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
  output: [3, 6, 7] # since only these three values are both in arr1 and arr2
  '''
  return list(set(arr1).intersection(set(arr2)))

def find_duplicates_sorted(arr1,arr2):
  '''
  input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
  output: [3, 6, 7] # since only these three values are both in arr1 and arr2
  '''
  l, r = 0, 0
  res = []
  while l < len(arr1) or r < len(arr2):
    if arr1[l] == arr2[r]:
      res.append(arr1[l])
      l, r = l+1, r+1
    elif arr1[l] > arr2[r]:
      r += 1
    else:
      l += 1


'''
l           r
[1, 2, 3]  [3, 6]
    l       r
[1, 2, 3]  [3, 6]
       l    r
[1, 2, 3]  [3, 6]
         l     r
[1, 2, 3]  [3, 6]

'''

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1,arr2))