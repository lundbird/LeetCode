def decodeVariations(S):
  def dfs(i):
    if i == 0:
      return 1
    
    if int(S[i-1])==1 or (int(S[i-1])==2 and int(S[i])<=6):
      if i-2 >= 0:
        return dfs(i-1) + dfs(i-2)
      else:
        return dfs(i-1) + 1
    else:
      return dfs(i-1)
    

  if '0' in S:
    return 0
  return dfs(len(S)-1)
print(decodeVariations('83778549129'))
print(decodeVariations('1262'))