def different_number(arr) -> int:
  '''
  [0,1,2,3] -> 4
  [1,2,3,4] -> 0
  [0,1,3,4] -> 2
  '''
  sorted_arr = sorted(arr)
  for i in range(len(sorted_arr)):
    if sorted_arr[i] != i:
      return i
  return len(sorted_arr)

def different_number_2(arr) -> int:
  '''
  [0,1,2,3] -> 4
  [1,2,3,4] -> 0
  [0,1,3,4] -> 2
  '''
  dummy_array = [0]*(len(arr)+1)
  for val in arr:
    dummy_array[val] = 1
  return dummy_array.get(0)
  


print(different_number([0,1,2,3]))
print(different_number([1,2,3,4]))
print(different_number([0,1,3,4]))
