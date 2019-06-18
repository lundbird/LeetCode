class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = set([S])
        for i in range(len(S)):
            if not S[i].isalpha():
                continue
            next_words = set()
            for word in res:
                next_words.add(word[:i]+word[i].upper()+word[i+1:])
                next_words.add(word[:i]+word[i].lower()+word[i+1:])
            res |= next_words
        return list(res)