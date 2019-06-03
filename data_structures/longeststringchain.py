from functools import lru_cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        M = set(words)
        @lru_cache(maxsize=None)
        def dfs(word): #returns list of words on this path
            children = []
            for i in range(len(word)-1):
                if word[:i]+word[i+1:] in M:
                    children.append(dfs(word[:i]+word[i+1:]))
            return max(children)+1 if children else 1
        return max(dfs(word) for word in words)