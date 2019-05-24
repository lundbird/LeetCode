def findAnagrams(self, s: str, p: str):
    result = []
    p_count = {}
    s_count = {}
    for char in p:
        p_count[char] = p_count.get(char,0) + 1
    for char in s[:len(p)]:
        s_count[char] = s_count.get(char,0) + 1
    if s_count == p_count: 
        result.append(0)
    for i in range(1,len(s)-len(p)+1):
        s_count[s[i+len(p)-1]] = s_count.get(s[i+len(p)-1],0) + 1
        s_count[s[i-1]] = s_count.get(s[i-1],0) - 1
        if s_count[s[i-1]]==0:
            del s_count[s[i-1]]
        if s_count == p_count: 
            result.append(i)
    return result

if __name__=="__main__":
    print(findAnagrams("cbaebabacd","abc"))
    print(findAnagrams("abab","ab"))